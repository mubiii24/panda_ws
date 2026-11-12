# panda_ws

A ROS 2 workspace for controlling and planning motion for the Franka Emika **Panda** robot arm in simulation. It has two packages:

- **`panda_control`** (Python): scripts that move the arm and gripper through ROS 2 action servers, from simple joint moves to a full pick-and-place with collision checking.
- **`panda_planning`** (C++): a MoveIt 2 demo that plans to named and pose goals, avoids an obstacle, and runs a Cartesian path.

## Requirements

- Ubuntu with **ROS 2 Humble**
- [MoveIt 2](https://moveit.ros.org/) and the Panda demo configuration:

```bash
sudo apt install ros-humble-moveit ros-humble-moveit-resources-panda-moveit-config
```

- `colcon` and `rosdep`

## Build

```bash
git clone https://github.com/mubiii24/panda_ws.git
cd panda_ws
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

> `src/franka_ros2`, `src/franka_description` and `src/moveit_resources` are empty in this repository. Clone them into `src/` yourself if you need them.

## Usage

Every script needs the Panda MoveIt demo running first. It starts RViz, MoveIt and the arm and gripper controllers (`panda_arm_controller`, `panda_hand_controller`):

```bash
# Terminal 1
source install/setup.bash
ros2 launch moveit_resources_panda_moveit_config demo.launch.py
```

Then run any of the following in a second terminal (after sourcing `install/setup.bash`).

### MoveIt planning demo (`panda_planning`)

```bash
ros2 launch panda_planning plan_demo.launch.py
```

Plans and executes these steps in order:

1. Move to the named `ready` pose.
2. Plan to a pose goal with the gripper pointing down.
3. Add a box obstacle and plan around it.
4. Remove the box and run a Cartesian down, sideways, up path.

### Control scripts (`panda_control`)

| Command | What it does |
| --- | --- |
| `ros2 run panda_control move_arm` | Moves the arm between a few fixed joint poses and back to ready. |
| `ros2 run panda_control pick_place` | Pick and place using fixed joint poses and gripper commands. |
| `ros2 run panda_control pick_place_object` | Interactive pick and place. Asks for pick and place positions, adds a table and a box to the planning scene, plans collision-free moves and attaches the box while carrying it. |
| `ros2 run panda_control manual_path` | Plays a hand-written joint path. Edit the `PATH` list at the top of the file. Joint limits are checked first. |
| `ros2 run panda_control record_path` | Records joint positions you set in RViz. Press Enter to save a point, `q` to finish. Saves to `~/panda_path.json`. |
| `ros2 run panda_control play_path` | Replays the path saved by `record_path`, with a speed limit. |

**Record and replay a path:**

```bash
ros2 run panda_control record_path   # move the arm in RViz, press Enter at each pose
ros2 run panda_control play_path     # replay it
```

**`pick_place_object` workspace limits.** Positions are in metres in the robot base frame. Keep `x` between 0.30 and 0.60, `y` between -0.40 and 0.40, and the distance from the base under 0.58. Pick and place points must be at least 0.10 m apart. Defaults are pick `(0.40, 0.25)` and place `(0.40, -0.25)`.

## Project structure

```
panda_ws/
└── src/
    ├── panda_control/        # Python package (ament_python)
    │   └── panda_control/
    │       ├── move_arm.py
    │       ├── pick_place.py
    │       ├── pick_place_object.py
    │       ├── manual_path.py
    │       ├── record_path.py
    │       └── play_path.py
    └── panda_planning/       # C++ package (ament_cmake)
        ├── src/plan_demo.cpp
        └── launch/plan_demo.launch.py
```

## Safety

These scripts are written for simulation. Before running anything on a real robot, check the joint poses, speeds and workspace limits in the code.

## License

`panda_control` declares the MIT license in its `package.xml`. See the `LICENSE` file for details.
