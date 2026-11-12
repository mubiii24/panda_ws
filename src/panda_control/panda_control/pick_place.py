import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory, GripperCommand
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration

ARM_ACTION = '/panda_arm_controller/follow_joint_trajectory'
HAND_ACTION = '/panda_hand_controller/gripper_cmd'

# Joint poses (radians). Approximate values, tune them for your setup.
READY = [0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785]
ABOVE_PICK = [0.0, 0.2, 0.0, -2.0, 0.0, 2.2, 0.785]
PICK = [0.0, 0.5, 0.0, -2.0, 0.0, 2.5, 0.785]
ABOVE_PLACE = [1.0, 0.2, 0.0, -2.0, 0.0, 2.2, 0.785]
PLACE = [1.0, 0.5, 0.0, -2.0, 0.0, 2.5, 0.785]


class PickPlace(Node):
    def __init__(self):
        super().__init__('pick_place')
        self.arm = ActionClient(self, FollowJointTrajectory, ARM_ACTION)
        self.hand = ActionClient(self, GripperCommand, HAND_ACTION)

    def _wait(self, future):
        rclpy.spin_until_future_complete(self, future)
        return future.result()

    def move(self, positions, secs=4):
        self.arm.wait_for_server()
        goal = FollowJointTrajectory.Goal()
        goal.trajectory.joint_names = [f'panda_joint{i}' for i in range(1, 8)]
        point = JointTrajectoryPoint()
        point.positions = positions
        point.time_from_start = Duration(sec=secs)
        goal.trajectory.points = [point]

        handle = self._wait(self.arm.send_goal_async(goal))
        if not handle.accepted:
            self.get_logger().error('Arm goal rejected')
            return False
        self._wait(handle.get_result_async())
        return True

    def gripper(self, position, effort=20.0):
        """position = finger opening in metres: 0.04 open, 0.0 closed."""
        self.hand.wait_for_server()
        goal = GripperCommand.Goal()
        goal.command.position = position
        goal.command.max_effort = effort

        handle = self._wait(self.hand.send_goal_async(goal))
        if not handle.accepted:
            self.get_logger().error('Gripper goal rejected')
            return False
        self._wait(handle.get_result_async())
        return True

    def run(self):
        log = self.get_logger().info
        log('Go to ready, open gripper')
        self.move(READY)
        self.gripper(0.04)

        log('Approach pick position')
        self.move(ABOVE_PICK)
        self.move(PICK, secs=3)

        log('Grasp')
        self.gripper(0.02)

        log('Lift and carry')
        self.move(ABOVE_PICK, secs=3)
        self.move(ABOVE_PLACE, secs=5)

        log('Place')
        self.move(PLACE, secs=3)
        self.gripper(0.04)

        log('Retreat and return to ready')
        self.move(ABOVE_PLACE, secs=3)
        self.move(READY)
        log('Done')


def main():
    rclpy.init()
    node = PickPlace()
    node.run()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
