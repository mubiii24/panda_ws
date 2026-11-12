import json
import os

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

JOINTS = [f'panda_joint{i}' for i in range(1, 8)]
FILE = os.path.expanduser('~/panda_path.json')


class Recorder(Node):
    def __init__(self):
        super().__init__('record_path')
        self.latest = None
        self.create_subscription(JointState, '/joint_states', self.cb, 10)

    def cb(self, msg):
        pos = dict(zip(msg.name, msg.position))
        if all(j in pos for j in JOINTS):
            self.latest = [pos[j] for j in JOINTS]


def main():
    rclpy.init()
    node = Recorder()
    points = []

    print('\nMove the arm in RViz (Plan & Execute) to a position.')
    print('Then press Enter here to record it. Type q + Enter to finish.\n')

    while True:
        cmd = input(f'[{len(points)} points saved] Enter = save, q = finish: ')
        if cmd.strip().lower() == 'q':
            break
        for _ in range(20):                 # refresh to newest joint state
            rclpy.spin_once(node, timeout_sec=0.05)
        if node.latest is None:
            print('No joint states received. Is the demo running?')
            continue
        points.append([round(x, 4) for x in node.latest])
        print(f'  saved point {len(points)}: {points[-1]}')

    with open(FILE, 'w') as f:
        json.dump(points, f, indent=2)
    print(f'\nSaved {len(points)} points to {FILE}')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
