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
CMAKE_SOURCE_DIR = /home/ecestudent/testOpenCV

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ecestudent/testOpenCV

# Include any dependencies generated for this target.
include CMakeFiles/camshift.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/camshift.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/camshift.dir/flags.make

CMakeFiles/camshift.dir/camshift.cpp.o: CMakeFiles/camshift.dir/flags.make
CMakeFiles/camshift.dir/camshift.cpp.o: camshift.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ecestudent/testOpenCV/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/camshift.dir/camshift.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/camshift.dir/camshift.cpp.o -c /home/ecestudent/testOpenCV/camshift.cpp

CMakeFiles/camshift.dir/camshift.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/camshift.dir/camshift.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/ecestudent/testOpenCV/camshift.cpp > CMakeFiles/camshift.dir/camshift.cpp.i

CMakeFiles/camshift.dir/camshift.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/camshift.dir/camshift.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/ecestudent/testOpenCV/camshift.cpp -o CMakeFiles/camshift.dir/camshift.cpp.s

CMakeFiles/camshift.dir/camshift.cpp.o.requires:
.PHONY : CMakeFiles/camshift.dir/camshift.cpp.o.requires

CMakeFiles/camshift.dir/camshift.cpp.o.provides: CMakeFiles/camshift.dir/camshift.cpp.o.requires
	$(MAKE) -f CMakeFiles/camshift.dir/build.make CMakeFiles/camshift.dir/camshift.cpp.o.provides.build
.PHONY : CMakeFiles/camshift.dir/camshift.cpp.o.provides

CMakeFiles/camshift.dir/camshift.cpp.o.provides.build: CMakeFiles/camshift.dir/camshift.cpp.o

# Object files for target camshift
camshift_OBJECTS = \
"CMakeFiles/camshift.dir/camshift.cpp.o"

# External object files for target camshift
camshift_EXTERNAL_OBJECTS =

camshift: CMakeFiles/camshift.dir/camshift.cpp.o
camshift: CMakeFiles/camshift.dir/build.make
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ts.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
camshift: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
camshift: CMakeFiles/camshift.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable camshift"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/camshift.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/camshift.dir/build: camshift
.PHONY : CMakeFiles/camshift.dir/build

CMakeFiles/camshift.dir/requires: CMakeFiles/camshift.dir/camshift.cpp.o.requires
.PHONY : CMakeFiles/camshift.dir/requires

CMakeFiles/camshift.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/camshift.dir/cmake_clean.cmake
.PHONY : CMakeFiles/camshift.dir/clean

CMakeFiles/camshift.dir/depend:
	cd /home/ecestudent/testOpenCV && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ecestudent/testOpenCV /home/ecestudent/testOpenCV /home/ecestudent/testOpenCV /home/ecestudent/testOpenCV /home/ecestudent/testOpenCV/CMakeFiles/camshift.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/camshift.dir/depend

