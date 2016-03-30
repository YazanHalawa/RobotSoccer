/*#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>

using namespace cv;
using namespace std;

int edgeThresh = 1;
int lowThreshold;
int const max_lowThreshold = 100;
int ratio = 3;
int kernel_size = 3;

Mat src2, src_gray2;
Mat dst2, detected_edges2;
 
//default capture width and height
const int FRAME_WIDTH = 640;
const int FRAME_HEIGHT = 480;


void CannyThreshold(int, void*)
{
  /// Reduce noise with a kernel 3x3
  blur( src_gray2, detected_edges2, Size(3,3) );

  /// Canny detector
  Canny( detected_edges2, detected_edges2, lowThreshold, lowThreshold*ratio, kernel_size );

  /// Using Canny's output as a mask, we display our result
  dst2 = Scalar::all(0);

  src2.copyTo( dst2, detected_edges2);
  imshow( "window_name222", dst2 );
 }

int main(int argc, char** argv)
{
    Mat src, src_gray;

    VideoCapture capture;
    //open capture object at location zero (default location for webcam)
    //capture.open(0);
    capture.open("http://192.168.1.48:8080/stream?topic=/image&dummy=param.mjpg");

    capture.set(CV_CAP_PROP_FRAME_WIDTH,FRAME_WIDTH);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT);

while(1){
    capture.read(src);
        capture.read(src2);

    //const char* filename = argc >= 2 ? argv[1] : "pic1.jpg";

    //Mat src = imread(filename, 0);
 if(src.empty())
 {
     cout << "can not open " << "filename" << endl;
     return -1;
 }

 Mat dst, cdst;



  /// Create a window
  namedWindow( "window_name", CV_WINDOW_AUTOSIZE );
  createTrackbar( "Min Threshold:", "window_name", &lowThreshold, max_lowThreshold, CannyThreshold );
  CannyThreshold(0,0);


 Canny(src, dst, lowThreshold, 100, 3);
 cvtColor(dst, cdst, CV_GRAY2BGR);
 
 //other tutorial begin
  cvtColor( src2, src_gray2, CV_BGR2GRAY );
  GaussianBlur( src_gray2, src_gray2, Size(9, 9), 2, 2 );
  vector<Vec3f> circles;
  HoughCircles( src_gray2, circles, CV_HOUGH_GRADIENT, 1, src_gray2.rows/8, 200, 10, 0, 0 );


  /// Draw the circles detected
  for( size_t i = 0; i < circles.size(); i++ )
  {
      Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
      int radius = cvRound(circles[i][2]);
      // circle center
      circle( src2, center, 3, Scalar(0,255,0), -1, 8, 0 );
      // circle outline
      circle( src2, center, radius, Scalar(0,0,255), 3, 8, 0 );
   } 

  vector<Vec4i> lines;
  HoughLinesP(dst, lines, 1, CV_PI/180, 20, 100, 3 );
  for( size_t i = 0; i < lines.size(); i++ )
  {
    Vec4i l = lines[i];
    line( cdst, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0,0,255), 3, CV_AA);
  }

  imshow("source", src2);
 imshow("detected lines", cdst);

 waitKey();
}
 return 0;
}

*/



#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>

using namespace cv;


//default capture width and height
const int FRAME_WIDTH = 640;
const int FRAME_HEIGHT = 480;
Mat src, src_gray;
int lowThreshold = 12;
int upperThreshold = 55;

void CannyThreshold(int, void*)
{
    vector<Vec3f> circles;
  /// Apply the Hough Transform to find the circles
  HoughCircles( src_gray, circles, CV_HOUGH_GRADIENT, 1, 1, upperThreshold, lowThreshold, 40, 50 );

if(circles.size() > 1){std::cout << "there are no circles" << circles.size() << "/n"; }
  /// Draw the circles detected
  for( size_t i = 0; i < circles.size(); i++ )
  {
      Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
      int radius = cvRound(circles[i][2]);
      // circle center
      circle( src, center, 3, Scalar(0,255,0), -1, 8, 0 );
      // circle outline
      circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );
        imshow( "Hough Circle Transform Demo", src );
   }
 }

/** @function main */
int main()
{


    VideoCapture capture;
    //open capture object at location zero (default location for webcam)
    //capture.open(0);
    capture.open("http://192.168.1.48:8080/stream?topic=/image&dummy=param.mjpg");

    capture.set(CV_CAP_PROP_FRAME_WIDTH,FRAME_WIDTH);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT);

while(1){
    capture.read(src);

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
//  CannyThreshold(0,0);

  /// Show your results
  namedWindow( "Hough Circle Transform Demo", CV_WINDOW_AUTOSIZE );
  //imshow( "Hough Circle Transform Demo", src );

  waitKey(0);
}
  return 0;
}
