# CMake generated Testfile for 
# Source directory: /home/mubii/panda_ws/src/franka_ros2/franka_gazebo/franka_gazebo_hardware
# Build directory: /home/mubii/panda_ws/build/franka_gazebo_hardware
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(gravity_compensation_model_test "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/mubii/panda_ws/build/franka_gazebo_hardware/test_results/franka_gazebo_hardware/gravity_compensation_model_test.gtest.xml" "--package-name" "franka_gazebo_hardware" "--output-file" "/home/mubii/panda_ws/build/franka_gazebo_hardware/ament_cmake_gmock/gravity_compensation_model_test.txt" "--command" "/home/mubii/panda_ws/build/franka_gazebo_hardware/gravity_compensation_model_test" "--gtest_output=xml:/home/mubii/panda_ws/build/franka_gazebo_hardware/test_results/franka_gazebo_hardware/gravity_compensation_model_test.gtest.xml")
set_tests_properties(gravity_compensation_model_test PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/mubii/panda_ws/build/franka_gazebo_hardware/gravity_compensation_model_test" TIMEOUT "60" WORKING_DIRECTORY "/home/mubii/panda_ws/build/franka_gazebo_hardware" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/mubii/panda_ws/src/franka_ros2/franka_gazebo/franka_gazebo_hardware/CMakeLists.txt;82;ament_add_gmock;/home/mubii/panda_ws/src/franka_ros2/franka_gazebo/franka_gazebo_hardware/CMakeLists.txt;0;")
subdirs("gmock")
subdirs("gtest")
