import math
import threading
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import Pose
from shape_msgs.msg import SolidPrimitive
from builtin_interfaces.msg import Duration
from std_msgs.msg import ColorRGBA
from control_msgs.action import GripperCommand, FollowJointTrajectory
from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import (
    Constraints, PositionConstraint, OrientationConstraint,
    CollisionObject, AttachedCollisionObject, PlanningScene, ObjectColor)
from moveit_msgs.srv import ApplyPlanningScene, GetCartesianPath

GROUP = 'panda_arm'
FRAME = 'panda_link0'
LINK = 'panda_link8'
HAND_LINK = 'panda_hand'
TOUCH_LINKS = ['panda_hand', 'panda_leftfinger', 'panda_rightfinger']

ARM_ACTION = '/panda_arm_controller/follow_joint_trajectory'
HAND_ACTION = '/panda_hand_controller/gripper_cmd'

OBJ_ID = 'pp_object'
TABLE_ID = 'pp_table'
OBJ_SIZE = (0.04, 0.04, 0.08)    # x, y, z of the box in metres
TCP_OFFSET = 0.1034              # panda_link8 to fingertip centre
APPROACH = 0.12                  # hover height above the grasp
# Gripper pointing down (x, y, z, w)
ORIENT = (0.92388, -0.38268, 0.0, 0.0)

DEFAULT_PICK = (0.40, 0.25)
DEFAULT_PLACE = (0.40, -0.25)

ERRORS = {
    -1: 'planning failed',
    -2: 'invalid motion plan',
    -4: 'control failed',
    -6: 'timed out',
    -10: 'start state in collision',
    -12: 'goal in collision',
    -31: 'no IK solution',
}


class PickPlace(Node):
    def __init__(self):
        super().__init__('pick_place_object')
        self.move = ActionClient(self, MoveGroup, '/move_action')
        self.hand = ActionClient(self, GripperCommand, HAND_ACTION)
        self.arm = ActionClient(self, FollowJointTrajectory, ARM_ACTION)
        self.scene = self.create_client(
            ApplyPlanningScene, '/apply_planning_scene')
        self.cart = self.create_client(
            GetCartesianPath, '/compute_cartesian_path')

    # ---------------- helpers ----------------
    @staticmethod
    def wait(future, timeout=180.0):
        t0 = time.time()
        while not future.done():
            if time.time() - t0 > timeout:
                raise RuntimeError('timed out waiting for a reply')
            time.sleep(0.02)
        return future.result()

    def log(self, text):
        self.get_logger().info(text)

    def check_connections(self):
        if not self.move.wait_for_server(timeout_sec=10.0):
            raise RuntimeError('/move_action not found. Is the demo running?')
        if not self.hand.wait_for_server(timeout_sec=10.0):
            raise RuntimeError(HAND_ACTION + ' not found')
        if not self.arm.wait_for_server(timeout_sec=10.0):
            raise RuntimeError(ARM_ACTION + ' not found')
        if not self.scene.wait_for_service(timeout_sec=10.0):
            raise RuntimeError('/apply_planning_scene not found')
        if not self.cart.wait_for_service(timeout_sec=10.0):
            raise RuntimeError('/compute_cartesian_path not found')

    # ---------------- planning scene ----------------
    def apply_scene(self, scene):
        req = ApplyPlanningScene.Request()
        req.scene = scene
        res = self.wait(self.scene.call_async(req))
        if not res.success:
            raise RuntimeError('planning scene update was refused')

    @staticmethod
    def make_box(obj_id, size, x, y, z):
        co = CollisionObject()
        co.header.frame_id = FRAME
        co.id = obj_id
        prim = SolidPrimitive()
        prim.type = SolidPrimitive.BOX
        prim.dimensions = [float(s) for s in size]
        p = Pose()
        p.position.x = float(x)
        p.position.y = float(y)
        p.position.z = float(z)
        p.orientation.w = 1.0
        co.primitives.append(prim)
        co.primitive_poses.append(p)
        co.operation = CollisionObject.ADD
        return co

    @staticmethod
    def make_remove(obj_id):
        co = CollisionObject()
        co.header.frame_id = FRAME
        co.id = obj_id
        co.operation = CollisionObject.REMOVE
        return co

    @staticmethod
    def make_color(obj_id, r, g, b, a=1.0):
        oc = ObjectColor()
        oc.id = obj_id
        oc.color = ColorRGBA(r=r, g=g, b=b, a=a)
        return oc

    def detach_object(self):
        aco = AttachedCollisionObject()
        aco.link_name = HAND_LINK
        aco.object.id = OBJ_ID
        aco.object.operation = CollisionObject.REMOVE
        s = PlanningScene()
        s.is_diff = True
        s.robot_state.is_diff = True
        s.robot_state.attached_collision_objects.append(aco)
        self.apply_scene(s)

    def safe_remove(self, obj_id):
        # Cleanup only: it is fine if the object does not exist yet.
        try:
            s = PlanningScene()
            s.is_diff = True
            s.world.collision_objects.append(self.make_remove(obj_id))
            self.apply_scene(s)
        except Exception:
            pass

    def setup_scene(self, pick_xy):
        # Clear leftovers from an earlier run (failures are ignored)
        try:
            self.detach_object()
        except Exception:
            pass
        self.safe_remove(OBJ_ID)
        self.safe_remove(TABLE_ID)

        s = PlanningScene()
        s.is_diff = True
        table = self.make_box(
            TABLE_ID, (0.6, 1.0, 0.02), 0.55, 0.0, -0.01)
        box = self.make_box(
            OBJ_ID, OBJ_SIZE, pick_xy[0], pick_xy[1], OBJ_SIZE[2] / 2.0)
        s.world.collision_objects.append(table)
        s.world.collision_objects.append(box)
        s.object_colors.append(self.make_color(TABLE_ID, 0.6, 0.6, 0.6))
        s.object_colors.append(self.make_color(OBJ_ID, 0.9, 0.1, 0.1))
        self.apply_scene(s)
        time.sleep(1.0)

    def attach_object(self, pick_xy):
        # take it out of the world, then attach the same box to the hand
        s = PlanningScene()
        s.is_diff = True
        s.world.collision_objects.append(self.make_remove(OBJ_ID))
        self.apply_scene(s)

        aco = AttachedCollisionObject()
        aco.link_name = HAND_LINK
        aco.object = self.make_box(
            OBJ_ID, OBJ_SIZE, pick_xy[0], pick_xy[1], OBJ_SIZE[2] / 2.0)
        aco.touch_links = TOUCH_LINKS
        s = PlanningScene()
        s.is_diff = True
        s.robot_state.is_diff = True
        s.robot_state.attached_collision_objects.append(aco)
        s.object_colors.append(self.make_color(OBJ_ID, 0.9, 0.1, 0.1))
        self.apply_scene(s)
        time.sleep(0.5)

    def put_object_down(self, place_xy):
        # release from the hand and put the box back into the world
        self.detach_object()
        s = PlanningScene()
        s.is_diff = True
        box = self.make_box(
            OBJ_ID, OBJ_SIZE, place_xy[0], place_xy[1], OBJ_SIZE[2] / 2.0)
        s.world.collision_objects.append(box)
        s.object_colors.append(self.make_color(OBJ_ID, 0.9, 0.1, 0.1))
        self.apply_scene(s)
        time.sleep(0.5)

    # ---------------- motion ----------------
    def move_to(self, x, y, z, label):
        """Collision-aware planned move of panda_link8 to (x, y, z)."""
        self.log('Planning: ' + label)
        c = Constraints()

        pc = PositionConstraint()
        pc.header.frame_id = FRAME
        pc.link_name = LINK
        prim = SolidPrimitive()
        prim.type = SolidPrimitive.SPHERE
        prim.dimensions = [0.005]
        p = Pose()
        p.position.x = float(x)
        p.position.y = float(y)
        p.position.z = float(z)
        p.orientation.w = 1.0
        pc.constraint_region.primitives.append(prim)
        pc.constraint_region.primitive_poses.append(p)
        pc.weight = 1.0

        oc = OrientationConstraint()
        oc.header.frame_id = FRAME
        oc.link_name = LINK
        oc.orientation.x = ORIENT[0]
        oc.orientation.y = ORIENT[1]
        oc.orientation.z = ORIENT[2]
        oc.orientation.w = ORIENT[3]
        oc.absolute_x_axis_tolerance = 0.02
        oc.absolute_y_axis_tolerance = 0.02
        oc.absolute_z_axis_tolerance = 0.02
        oc.weight = 1.0

        c.position_constraints.append(pc)
        c.orientation_constraints.append(oc)

        goal = MoveGroup.Goal()
        req = goal.request
        req.group_name = GROUP
        req.planner_id = 'RRTConnectkConfigDefault'
        req.num_planning_attempts = 10
        req.allowed_planning_time = 5.0
        req.max_velocity_scaling_factor = 0.3
        req.max_acceleration_scaling_factor = 0.3
        req.start_state.is_diff = True
        req.goal_constraints = [c]
        goal.planning_options.plan_only = False
        diff = goal.planning_options.planning_scene_diff
        diff.is_diff = True
        diff.robot_state.is_diff = True

        handle = self.wait(self.move.send_goal_async(goal))
        if not handle.accepted:
            raise RuntimeError(label + ': goal rejected by move_group')
        result = self.wait(handle.get_result_async())
        code = result.result.error_code.val
        if code != 1:
            msg = ERRORS.get(code, 'error code ' + str(code))
            raise RuntimeError(label + ': ' + msg)

    def straight_to(self, x, y, z, label, speed=0.25):
        """Straight-line move without collision checking, used for the
        last few centimetres at the object."""
        self.log('Straight move: ' + label)
        req = GetCartesianPath.Request()
        req.header.frame_id = FRAME
        req.start_state.is_diff = True
        req.group_name = GROUP
        req.link_name = LINK
        p = Pose()
        p.position.x = float(x)
        p.position.y = float(y)
        p.position.z = float(z)
        p.orientation.x = ORIENT[0]
        p.orientation.y = ORIENT[1]
        p.orientation.z = ORIENT[2]
        p.orientation.w = ORIENT[3]
        req.waypoints.append(p)
        req.max_step = 0.01
        req.jump_threshold = 0.0
        req.avoid_collisions = False

        res = self.wait(self.cart.call_async(req))
        if res.fraction < 0.99:
            pct = res.fraction * 100
            raise RuntimeError(
                label + ': only ' + format(pct, '.0f') +
                '% of the straight path is reachable. '
                'Move the position closer to the robot.')

        traj = res.solution.joint_trajectory
        t = 0.2
        prev = None
        for pt in traj.points:
            if prev is not None:
                diffs = [abs(a - b) for a, b in zip(pt.positions, prev)]
                d = max(diffs)
                t += max(0.05, d / speed)
            pt.velocities = []
            pt.accelerations = []
            sec = int(t)
            nanosec = int((t - sec) * 1e9)
            pt.time_from_start = Duration(sec=sec, nanosec=nanosec)
            prev = list(pt.positions)

        goal = FollowJointTrajectory.Goal()
        goal.trajectory = traj
        handle = self.wait(self.arm.send_goal_async(goal))
        if not handle.accepted:
            raise RuntimeError(label + ': controller rejected the path')
        result = self.wait(handle.get_result_async())
        code = result.result.error_code
        if code != 0:
            raise RuntimeError(
                label + ': controller error code ' + str(code))

    def gripper(self, position, label):
        self.log('Gripper: ' + label)
        g = GripperCommand.Goal()
        g.command.position = float(position)
        g.command.max_effort = 20.0
        handle = self.wait(self.hand.send_goal_async(g))
        if not handle.accepted:
            raise RuntimeError('gripper goal rejected')
        self.wait(handle.get_result_async())

    # ---------------- the task ----------------
    def run(self, pick, place):
        zc = OBJ_SIZE[2] / 2.0            # box centre height on the table
        grasp_z = zc + TCP_OFFSET         # panda_link8 height at the grasp
        hover_z = grasp_z + APPROACH
        place_z = grasp_z + 0.003         # tiny clearance when setting down
        finger = OBJ_SIZE[0] / 2.0        # per-finger opening that grips it

        self.check_connections()
        self.log('Pick at ' + str(pick) + ', place at ' + str(place))
        self.setup_scene(pick)

        print('\nA grey table and a red box should now be visible in RViz.')
        print('(Displays > MotionPlanning > Scene Geometry >')
        print(' Show Scene Geometry)')
        input('Press Enter to start the pick and place... ')

        self.gripper(0.04, 'open')
        self.move_to(pick[0], pick[1], hover_z, 'above the object')
        self.straight_to(pick[0], pick[1], grasp_z, 'down to the object')
        self.gripper(finger, 'close on the object')
        self.attach_object(pick)
        self.straight_to(pick[0], pick[1], hover_z, 'lift')
        self.move_to(place[0], place[1], hover_z, 'above the place position')
        self.straight_to(place[0], place[1], place_z, 'down to the table')
        self.gripper(0.04, 'release')
        self.put_object_down(place)
        self.straight_to(place[0], place[1], hover_z, 'retreat up')
        self.log('Done: object placed')


def ask_xy(text, default):
    prompt = text + ' (x y in metres) [' + str(default[0]) + ' '
    prompt += str(default[1]) + ']: '
    raw = input(prompt).strip()
    if not raw:
        return default
    x, y = [float(v) for v in raw.replace(',', ' ').split()]
    return (x, y)


def check_reach(name, xy):
    x, y = xy
    r = math.hypot(x, y)
    if not (0.30 <= x <= 0.60 and abs(y) <= 0.40 and 0.30 <= r <= 0.58):
        raise ValueError(
            name + ' (' + str(x) + ', ' + str(y) + ') is out of reach. '
            'Use x 0.30 to 0.60, y -0.40 to 0.40, and keep the distance '
            'from the base under 0.58.')


def main():
    rclpy.init()
    node = PickPlace()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    threading.Thread(target=executor.spin, daemon=True).start()
    try:
        print('\nPress Enter to accept the value in brackets.')
        pick = ask_xy('Where is the object? PICK', DEFAULT_PICK)
        place = ask_xy('Where should it go? PLACE', DEFAULT_PLACE)
        check_reach('Pick', pick)
        check_reach('Place', place)
        dist = math.hypot(pick[0] - place[0], pick[1] - place[1])
        if dist < 0.10:
            raise ValueError(
                'Pick and place are too close together. '
                'Keep them at least 0.10 m apart.')
        node.run(pick, place)
    except Exception as e:
        node.get_logger().error(str(e))
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
