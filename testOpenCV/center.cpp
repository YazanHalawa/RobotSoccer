

//http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/hough_circle/hough_circle.html

#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

//default capture width and height
const int FRAME_WIDTH = 840;
const int FRAME_HEIGHT = 480;
Mat src, src_gray;
int lowThreshold = 26;
int upperThreshold = 82;


string intToString(int number){


  std::stringstream ss;
  ss << number;
  return ss.str();
}
void CannyThreshold(int, void*)
{
    vector<Vec3f> circles;
  /// Apply the Hough Transform to find the circles
  HoughCircles( src_gray, circles, CV_HOUGH_GRADIENT, 1, 4, upperThreshold, lowThreshold, 40, 50 );

if(circles.size() > 1){std::cout << "there are no circles" << circles.size() << "/n"; }
  /// Draw the circles detected
      int one = 0; 
      int two = 0;
      int three = 0;
      int circle_size = circles.size();

    for( size_t i = 0; i < circle_size ; i++ ){

      one += cvRound(circles[i][0]); 
      two += cvRound(circles[i][1]);
      three += cvRound(circles[i][2]);
      // circle center
    }

    if (circle_size)
    {
one = one/circle_size;
two = two/circle_size;
three = three/circle_size;

          Point center( one, two);
    int radius = three;
   
      circle( src, center, 3, Scalar(0,255,0), -1, 8, 0 );
      // circle outline
      circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );


  cv::putText(src,intToString(one),cv::Point(20,20),1,1,Scalar(0,255,0));
  cv::putText(src,intToString(two),cv::Point(50,50),1,1,Scalar(0,255,0));
  cv::putText(src,intToString(three),cv::Point(80,80),1,1,Scalar(0,255,0));

        imshow( "Hough Circle Transform Demo", src );
    }
   
 }

/** @function main */
int main()
{

    Mat cameraFeed;
    VideoCapture capture;
    //open capture object at location zero (default location for webcam)
    //capture.open(0);
    capture.open("http://192.168.1.78:8080/stream?topic=/image&dummy=param.mjpg");

    capture.set(CV_CAP_PROP_FRAME_WIDTH,FRAME_WIDTH);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT);

while(1){

    capture.read(cameraFeed);
    cv::flip(cameraFeed, src, -1); 


  if( !src.data )
    { return -1; }

  /// Convert it to gray
  cvtColor( src, src_gray, CV_BGR2GRAY );

  /// Reduce the noise so we avoid false circle detection
  GaussianBlur( src_gray, src_gray, Size(9, 9), 2, 2 );



 /// Create a window
  namedWindow( "window_name", CV_WINDOW_AUTOSIZE );
  createTrackbar( "Min Threshold:", "window_name", &lowThreshold, 150, CannyThreshold );
  createTrackbar( "Max Threshold:", "window_name", &upperThreshold, 300, CannyThreshold );
  CannyThreshold(0,0);

  /// Show your results
  namedWindow( "Hough Circle Transform Demo", CV_WINDOW_AUTOSIZE );
  imshow( "Hough Circle Transform Demo", src );

  waitKey(0);
}
  return 0;
}