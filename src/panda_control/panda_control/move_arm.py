import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration


class ArmMover(Node):
    def __init__(self):
        super().__init__('move_arm')
        self.client = ActionClient(
            self,
            FollowJointTrajectory,
            '/panda_arm_controller/follow_joint_trajectory')

    def move(self, positions, secs=4):
        self.get_logger().info('Waiting for controller action server...')
        self.client.wait_for_server()

        goal = FollowJointTrajectory.Goal()
        goal.trajectory.joint_names = [f'panda_joint{i}' for i in range(1, 8)]

        point = JointTrajectoryPoint()
        point.positions = positions
        point.time_from_start = Duration(sec=secs)
        goal.trajectory.points = [point]

        send_future = self.client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, send_future)
        handle = send_future.result()

        if not handle.accepted:
            self.get_logger().error('Goal rejected')
            return

        result_future = handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info('Move finished')


def main():
    rclpy.init()
    node = ArmMover()

    ready = [0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785]
    second = [0.5, -0.5, 0.0, -2.0, 0.0, 1.5, 0.785]

    node.move(ready)
    node.move(second)
    node.move(ready)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
