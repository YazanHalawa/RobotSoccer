cmake_minimum_required(VERSION 2.8)
project( DisplayImage )
find_package( OpenCV REQUIRED )
add_executable( DisplayImage DisplayImage.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )

project( RedDetectingDemo )
find_package( OpenCV REQUIRED )
add_executable( RedDetectingDemo RedDetectingDemo.cpp )
target_link_libraries( RedDetectingDemo ${OpenCV_LIBS} )

project( RedTrackingDemo )
find_package( OpenCV REQUIRED )
add_executable( RedTrackingDemo RedTrackingDemo.cpp )
target_link_libraries( RedTrackingDemo ${OpenCV_LIBS} )



project( contour )
find_package( OpenCV REQUIRED )
add_executable( contour contour.cpp )
target_link_libraries( contour ${OpenCV_LIBS} )

project( circle )
find_package( OpenCV REQUIRED )
add_executable( circle circle.cpp )
target_link_libraries( circle ${OpenCV_LIBS} )

project( circle2 )
find_package( OpenCV REQUIRED )
add_executable( circle2 circle2.cpp )
target_link_libraries( circle2 ${OpenCV_LIBS} )

project( center )
find_package( OpenCV REQUIRED )
add_executable( center center.cpp )
target_link_libraries( center ${OpenCV_LIBS} )


project( selection )
find_package( OpenCV REQUIRED )
add_executable( selection selection.cpp )
target_link_libraries( selection ${OpenCV_LIBS} )


project( calibrating )
find_package( OpenCV REQUIRED )
add_executable( calibrating calibrating.cpp )
target_link_libraries( calibrating ${OpenCV_LIBS} )


project( histo )
find_package( OpenCV REQUIRED )
add_executable( histo histo.cpp )
target_link_libraries( histo ${OpenCV_LIBS} )


project( backgroundsub )
find_package( OpenCV REQUIRED )
add_executable( backgroundsub backgroundsub.cpp )
target_link_libraries( backgroundsub ${OpenCV_LIBS} )

project( camshift )
find_package( OpenCV REQUIRED )
add_executable( camshift camshift.cpp )
target_link_libraries( camshift ${OpenCV_LIBS} )

project( rosvis )
find_package( OpenCV REQUIRED )
add_executable( rosvis rosvis.cpp )
target_link_libraries( rosvis ${OpenCV_LIBS} )