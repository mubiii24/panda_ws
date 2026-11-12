#include <memory>
#include <thread>
#include <vector>

#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/msg/collision_object.hpp>
#include <shape_msgs/msg/solid_primitive.hpp>
#include <geometry_msgs/msg/pose.hpp>

using moveit::planning_interface::MoveGroupInterface;

static bool plan_and_execute(MoveGroupInterface &group, const rclcpp::Logger &log,
                             const std::string &label)
{
  MoveGroupInterface::Plan plan;
  bool ok = (group.plan(plan) == moveit::core::MoveItErrorCode::SUCCESS);
  if (!ok) {
    RCLCPP_ERROR(log, "[%s] planning FAILED", label.c_str());
    return false;
  }
  RCLCPP_INFO(log, "[%s] plan found, executing", label.c_str());
  group.execute(plan);
  return true;
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  rclcpp::NodeOptions options;
  options.automatically_declare_parameters_from_overrides(true);
  auto node = rclcpp::Node::make_shared("panda_planner", options);

  rclcpp::executors::SingleThreadedExecutor executor;
  executor.add_node(node);
  std::thread spinner([&executor]() { executor.spin(); });

  auto log = node->get_logger();

  MoveGroupInterface group(node, "panda_arm");
  moveit::planning_interface::PlanningSceneInterface scene;

  // Planner settings
  group.setPlanningPipelineId("ompl");
  group.setPlannerId("RRTConnectkConfigDefault");
  group.setPlanningTime(5.0);
  group.setNumPlanningAttempts(10);
  group.setMaxVelocityScalingFactor(0.3);
  group.setMaxAccelerationScalingFactor(0.3);

  RCLCPP_INFO(log, "Planning frame: %s, end effector link: %s",
              group.getPlanningFrame().c_str(),
              group.getEndEffectorLink().c_str());

  // 1. Named target from the SRDF
  group.setNamedTarget("ready");
  plan_and_execute(group, log, "named target: ready");

  // 2. Pose goal (end effector pointing down)
  geometry_msgs::msg::Pose goal;
  goal.orientation.x = 1.0;
  goal.orientation.y = 0.0;
  goal.orientation.z = 0.0;
  goal.orientation.w = 0.0;
  goal.position.x = 0.4;
  goal.position.y = 0.3;
  goal.position.z = 0.4;
  group.setPoseTarget(goal);
  plan_and_execute(group, log, "pose goal A");

  // 3. Add a box obstacle, then plan to the opposite side
  moveit_msgs::msg::CollisionObject box;
  box.header.frame_id = group.getPlanningFrame();
  box.id = "obstacle_box";

  shape_msgs::msg::SolidPrimitive prim;
  prim.type = prim.BOX;
  prim.dimensions = {0.1, 0.1, 0.6};   // x, y, z in metres

  geometry_msgs::msg::Pose box_pose;
  box_pose.orientation.w = 1.0;
  box_pose.position.x = 0.4;
  box_pose.position.y = 0.0;
  box_pose.position.z = 0.3;

  box.primitives.push_back(prim);
  box.primitive_poses.push_back(box_pose);
  box.operation = box.ADD;
  scene.applyCollisionObjects({box});
  rclcpp::sleep_for(std::chrono::seconds(1));   // let the scene update

  goal.position.y = -0.3;
  group.setPoseTarget(goal);
  plan_and_execute(group, log, "pose goal B (around the box)");

  // Remove the box again
  scene.removeCollisionObjects({"obstacle_box"});
  rclcpp::sleep_for(std::chrono::seconds(1));

  // 4. Cartesian straight-line path
  group.setStartStateToCurrentState();
  std::vector<geometry_msgs::msg::Pose> waypoints;
  geometry_msgs::msg::Pose p = group.getCurrentPose().pose;
  p.position.z -= 0.10;  waypoints.push_back(p);   // down
  p.position.y += 0.15;  waypoints.push_back(p);   // sideways
  p.position.z += 0.10;  waypoints.push_back(p);   // up

  moveit_msgs::msg::RobotTrajectory trajectory;
  double fraction = group.computeCartesianPath(waypoints, 0.01, 0.0, trajectory);
  RCLCPP_INFO(log, "Cartesian path: %.1f%% achieved", fraction * 100.0);
  if (fraction > 0.95) {
    group.execute(trajectory);
  }

  rclcpp::shutdown();
  spinner.join();
  return 0;
}
