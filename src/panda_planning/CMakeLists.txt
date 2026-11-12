cmake_minimum_required(VERSION 3.8)
project(panda_planning)

set(CMAKE_CXX_STANDARD 17)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(shape_msgs REQUIRED)

add_executable(plan_demo src/plan_demo.cpp)
ament_target_dependencies(plan_demo
  rclcpp moveit_ros_planning_interface moveit_msgs geometry_msgs shape_msgs)

install(TARGETS plan_demo DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
