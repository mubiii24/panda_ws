import json
import os

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration

ACTION = '/panda_arm_controller/follow_joint_trajectory'
JOINTS = [f'panda_joint{i}' for i in range(1, 8)]
FILE = os.path.expanduser('~/panda_path.json')

MAX_SPEED = 0.4      # rad/s, lower = slower and safer
MIN_SEGMENT = 1.0    # seconds, minimum time per move


def to_duration(seconds):
    sec = int(seconds)
    return Duration(sec=sec, nanosec=int((seconds - sec) * 1e9))


def main():
    rclpy.init()
    node = Node('play_path')
    client = ActionClient(node, FollowJointTrajectory, ACTION)

    with open(FILE) as f:
        points = json.load(f)
    node.get_logger().info(f'Loaded {len(points)} points from {FILE}')

    client.wait_for_server()
    goal = FollowJointTrajectory.Goal()
    goal.trajectory.joint_names = JOINTS

    t = 2.0                                   # time to reach the first point
    prev = None
    for pos in points:
        if prev is not None:
            dist = max(abs(a - b) for a, b in zip(pos, prev))
            t += max(MIN_SEGMENT, dist / MAX_SPEED)
        p = JointTrajectoryPoint()
        p.positions = [float(x) for x in pos]
        p.velocities = [0.0] * 7              # stop at every recorded point
        p.time_from_start = to_duration(t)
        goal.trajectory.points.append(p)
        prev = pos

    node.get_logger().info(f'Playing path, total {t:.1f} s')
    fut = client.send_goal_async(goal)
    rclpy.spin_until_future_complete(node, fut)
    handle = fut.result()
    if not handle.accepted:
        node.get_logger().error('Path rejected')
    else:
        res = handle.get_result_async()
        rclpy.spin_until_future_complete(node, res)
        node.get_logger().info(f'Done, error code {res.result().result.error_code}')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
