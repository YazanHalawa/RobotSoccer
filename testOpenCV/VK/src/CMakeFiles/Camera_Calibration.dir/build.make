# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ecestudent/testOpenCV/VK/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ecestudent/testOpenCV/VK/src

# Include any dependencies generated for this target.
include CMakeFiles/Camera_Calibration.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Camera_Calibration.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Camera_Calibration.dir/flags.make

CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o: CMakeFiles/Camera_Calibration.dir/flags.make
CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o: camera_calibration.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ecestudent/testOpenCV/VK/src/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o -c /home/ecestudent/testOpenCV/VK/src/camera_calibration.cpp

CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/ecestudent/testOpenCV/VK/src/camera_calibration.cpp > CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.i

CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/ecestudent/testOpenCV/VK/src/camera_calibration.cpp -o CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.s

CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.requires:
.PHONY : CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.requires

CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.provides: CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.requires
	$(MAKE) -f CMakeFiles/Camera_Calibration.dir/build.make CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.provides.build
.PHONY : CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.provides

CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.provides.build: CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o

# Object files for target Camera_Calibration
Camera_Calibration_OBJECTS = \
"CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o"

# External object files for target Camera_Calibration
Camera_Calibration_EXTERNAL_OBJECTS =

Camera_Calibration: CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o
Camera_Calibration: CMakeFiles/Camera_Calibration.dir/build.make
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
Camera_Calibration: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
Camera_Calibration: CMakeFiles/Camera_Calibration.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable Camera_Calibration"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Camera_Calibration.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Camera_Calibration.dir/build: Camera_Calibration
.PHONY : CMakeFiles/Camera_Calibration.dir/build

CMakeFiles/Camera_Calibration.dir/requires: CMakeFiles/Camera_Calibration.dir/camera_calibration.cpp.o.requires
.PHONY : CMakeFiles/Camera_Calibration.dir/requires

CMakeFiles/Camera_Calibration.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Camera_Calibration.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Camera_Calibration.dir/clean

CMakeFiles/Camera_Calibration.dir/depend:
	cd /home/ecestudent/testOpenCV/VK/src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ecestudent/testOpenCV/VK/src /home/ecestudent/testOpenCV/VK/src /home/ecestudent/testOpenCV/VK/src /home/ecestudent/testOpenCV/VK/src /home/ecestudent/testOpenCV/VK/src/CMakeFiles/Camera_Calibration.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Camera_Calibration.dir/depend

