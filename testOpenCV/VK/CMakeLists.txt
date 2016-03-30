cmake_minimum_required(VERSION 2.8)
project( computer_vision )
find_package( OpenCV REQUIRED )
add_executable(computer_vision ComputerVision.cpp Ball.cpp Object.cpp Robot.cpp)
target_link_libraries(computer_vision ${OpenCV_LIBS} -lpthread)

project( cal )
find_package( OpenCV REQUIRED )
add_executable( cal camera_calibration.cpp)
target_link_libraries(cal ${OpenCV_LIBS} -lpthread)

#target_link_libraries(${PROJECT_NAME} [...] -lpthread [...]) #obviously without the '[...]' and the correct target name
