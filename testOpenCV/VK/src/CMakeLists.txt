cmake_minimum_required(VERSION 2.8.3)
project( robot_soccer )

find_package(
catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  sensor_msgs
  cv_bridge
  image_transport
)



###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES robot_soccer
  CATKIN_DEPENDS roscpp rospy std_msgs message_generation message_runtime sensor_msgs cv_bridge image_transport
#  DEPENDS system_lib
)


include_directories(${catkin_INCLUDE_DIRS} include)
add_executable( computer_vision src/ComputerVision.cpp src/Ball.cpp src/Object.cpp src/Robot.cpp)
target_link_libraries( computer_vision ${catkin_LIBRARIES} )

#cmake_minimum_required(VERSION 2.8)
#project( Camera_Calibration )
#find_package( OpenCV REQUIRED )
#add_executable( Camera_Calibration camera_calibration.cpp )
#target_link_libraries( Camera_Calibration ${OpenCV_LIBS} )

#include_directories(${catkin_INCLUDE_DIRS}, include/robot_soccer)
#
#add_executable(computer_vision src/ComputerVision.cpp src/Ball.cpp src/Object.cpp src/Robot.cpp)

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS } -pthread")
#set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS } -pthread")