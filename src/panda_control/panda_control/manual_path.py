import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration

ACTION = '/panda_arm_controller/follow_joint_trajectory'
JOINTS = [f'panda_joint{i}' for i in range(1, 8)]

# Panda joint limits (radians): (min, max)
LIMITS = [
    (-2.8973, 2.8973), (-1.7628, 1.7628), (-2.8973, 2.8973),
    (-3.0718, -0.0698), (-2.8973, 2.8973), (-0.0175, 3.7525),
    (-2.8973, 2.8973),
]

# ---------------------------------------------------------------
# EDIT THIS: your manual path. Each row is
#   (seconds to take to reach this point, [j1, j2, j3, j4, j5, j6, j7])
# ---------------------------------------------------------------
PATH = [
    (4.0, [0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785]),   # start / ready
    (3.0, [0.5, -0.4, 0.0, -2.2, 0.0, 1.8, 0.785]),         # point 1
    (3.0, [0.5, 0.0, 0.0, -1.8, 0.0, 1.8, 0.785]),          # point 2
    (3.0, [-0.5, 0.0, 0.0, -1.8, 0.0, 1.8, 0.785]),         # point 3
    (4.0, [0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785]),   # back to ready
]

# True  = arm stops briefly at every point (precise, safe)
# False = arm flows through the points without stopping (smoother)
STOP_AT_EACH_POINT = True


def to_duration(seconds):
    sec = int(seconds)
    nanosec = int((seconds - sec) * 1e9)
    return Duration(sec=sec, nanosec=nanosec)


class ManualPath(Node):
    def __init__(self):
        super().__init__('manual_path')
        self.client = ActionClient(self, FollowJointTrajectory, ACTION)

    def check_limits(self):
        ok = True
        for n, (_, pos) in enumerate(PATH, start=1):
            if len(pos) != 7:
                self.get_logger().error(f'Point {n}: needs 7 joint values')
                ok = False
                continue
            for j, (lo, hi) in enumerate(LIMITS):
                if not lo <= pos[j] <= hi:
                    self.get_logger().error(
                        f'Point {n}: joint {j + 1} = {pos[j]:.3f} '
                        f'is outside [{lo}, {hi}]')
                    ok = False
        return ok

    def run(self):
        if not self.check_limits():
            self.get_logger().error('Fix the path and run again')
            return

        self.get_logger().info('Waiting for controller...')
        self.client.wait_for_server()

        goal = FollowJointTrajectory.Goal()
        goal.trajectory.joint_names = JOINTS

        elapsed = 0.0
        for seconds, pos in PATH:
            elapsed += seconds
            point = JointTrajectoryPoint()
            point.positions = [float(x) for x in pos]
            if STOP_AT_EACH_POINT:
                point.velocities = [0.0] * 7
            point.time_from_start = to_duration(elapsed)
            goal.trajectory.points.append(point)

        self.get_logger().info(
            f'Sending path with {len(PATH)} points, total {elapsed:.1f} s')
        send_future = self.client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, send_future)
        handle = send_future.result()

        if not handle.accepted:
            self.get_logger().error('Path rejected by controller')
            return

        result_future = handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        code = result_future.result().result.error_code
        if code == 0:
            self.get_logger().info('Path finished successfully')
        else:
            self.get_logger().error(f'Path ended with error code {code}')


def main():
    rclpy.init()
    node = ManualPath()
    node.run()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
