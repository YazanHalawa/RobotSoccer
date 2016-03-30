/*#include <cv.h>
#include <highgui.h>
#include <math.h>

using namespace cv;


//default capture width and height
const int FRAME_WIDTH = 640;
const int FRAME_HEIGHT = 480;

int main()
{
    Mat img, gray;

    VideoCapture capture;
    //open capture object at location zero (default location for webcam)
    //capture.open(0);
    capture.open("http://192.168.1.48:8080/stream?topic=/image&dummy=param.mjpg");

    capture.set(CV_CAP_PROP_FRAME_WIDTH,FRAME_WIDTH);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT);

    capture.read(img);

    cvtColor(img, gray, CV_BGR2GRAY);
    // smooth it, otherwise a lot of false circles may be detected
    GaussianBlur( gray, gray, Size(9, 9), 2, 2 );
    vector<Vec3f> circles;
    HoughCircles(gray, circles, CV_HOUGH_GRADIENT,
                 2, 480/4, 200, 100 );
    for( size_t i = 0; i < circles.size(); i++ )
    {
         Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
         int radius = cvRound(circles[i][2]);
         // draw the circle center
         circle( img, center, 3, Scalar(0,255,0), -1, 8, 0 );
         // draw the circle outline
         circle( img, center, radius, Scalar(0,0,255), 3, 8, 0 );
    }
    namedWindow( "circles", 1 );
    imshow( "circles", img );
    return 0;
}
*/

/*

#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>
 
using namespace cv;
using namespace std;
 
//default capture width and height
const int FRAME_WIDTH = 640;
const int FRAME_HEIGHT = 480;

int main()
{
  Mat src, gray;

  //src = imread( "building.jpg", 1 );resize(src,src,Size(640,480));
  
      VideoCapture capture;
    //open capture object at location zero (default location for webcam)
    //capture.open(0);
    capture.open("http://192.168.1.48:8080/stream?topic=/image&dummy=param.mjpg");

    capture.set(CV_CAP_PROP_FRAME_WIDTH,FRAME_WIDTH);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT);

    capture.read(src);


  cvtColor( src, gray, CV_BGR2GRAY );
 
  // Reduce the noise so we avoid false circle detection
  GaussianBlur( gray, gray, Size(9, 9), 2, 2 );
 
  vector<Vec3f> circles;
 
  // Apply the Hough Transform to find the circles
  HoughCircles( gray, circles, CV_HOUGH_GRADIENT, 1, 30, 200, 50, 10, 200 );
 
  // Draw the circles detected
  for( size_t i = 0; i < circles.size(); i++ )
  {
      Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
      int radius = cvRound(circles[i][2]);     
      circle( src, center, 3, Scalar(0,255,0), -1, 8, 0 );// circle center     
      circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );// circle outline
      cout << "center : " << center << "\nradius : " << radius << endl;
   }
 
  // Show your results
  namedWindow( "Hough Circle Transform Demo", CV_WINDOW_AUTOSIZE );
  imshow( "Hough Circle Transform Demo", src );
 
  waitKey(0);
  return 0;
}

*/



#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>

using namespace cv;
using namespace std;


//Mat src, src_gray;
//Mat dst, detected_edges;

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

void help()
{
 cout << "\nThis program demonstrates line finding with the Hough transform.\n"
         "Usage:\n"
         "./houghlines <image_name>, Default is pic1.jpg\n" << endl;
}

void CannyThreshold(int, void*)
{
  /// Reduce noise with a kernel 3x3
  blur( src_gray2, detected_edges2, Size(3,3) );

  /// Canny detector
  Canny( detected_edges2, detected_edges2, lowThreshold, lowThreshold*ratio, kernel_size );

  /// Using Canny's output as a mask, we display our result
  dst2 = Scalar::all(0);

  src2.copyTo( dst2, detected_edges2);
  imshow( "window_name", dst2 );
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

    capture.read(src);
        capture.read(src2);

    //const char* filename = argc >= 2 ? argv[1] : "pic1.jpg";

    //Mat src = imread(filename, 0);
 if(src.empty())
 {
     help();
     cout << "can not open " << "filename" << endl;
     return -1;
 }

 Mat dst, cdst;



  /// Create a window
  namedWindow( "window_name", CV_WINDOW_AUTOSIZE );

  /// Create a Trackbar for user to enter threshold
  createTrackbar( "Min Threshold:", "window_name", &lowThreshold, max_lowThreshold, CannyThreshold );

  /// Show the image
  CannyThreshold(0, 0);


 Canny(src, dst, lowThreshold, 200, 3);
 cvtColor(dst, cdst, CV_GRAY2BGR);
 
 //other tutorial begin
 cvtColor( src2, src_gray2, CV_BGR2GRAY );
   /// Reduce the noise so we avoid false circle detection
  GaussianBlur( src_gray2, src_gray2, Size(9, 9), 2, 2 );

  vector<Vec3f> circles;

 /// Apply the Hough Transform to find the circles
 HoughCircles( src_gray2, circles, CV_HOUGH_GRADIENT, 1, src_gray2.rows/8, 200, 100, 0, 0 );

  /// Draw the circles detected
  for( size_t i = 0; i < circles.size(); i++ )
  {
      Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
      int radius = cvRound(circles[i][2]);
      // circle center
      circle( src, center, 3, Scalar(0,255,0), -1, 8, 0 );
      // circle outline
      circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );
   }

  /// Show your results
  namedWindow( "Hough Circle Transform Demo", CV_WINDOW_AUTOSIZE );
  imshow( "Hough Circle Transform Demo", src );

//other tutorial end

 #if 0
  vector<Vec2f> lines;
  HoughLines(dst, lines, 1, CV_PI/180, 100, 0, 0 );

  for( size_t i = 0; i < lines.size(); i++ )
  {
     float rho = lines[i][0], theta = lines[i][1];
     Point pt1, pt2;
     double a = cos(theta), b = sin(theta);
     double x0 = a*rho, y0 = b*rho;
     pt1.x = cvRound(x0 + 1000*(-b));
     pt1.y = cvRound(y0 + 1000*(a));
     pt2.x = cvRound(x0 - 1000*(-b));
     pt2.y = cvRound(y0 - 1000*(a));
     line( cdst, pt1, pt2, Scalar(0,0,255), 3, CV_AA);
  }
 #else
  vector<Vec4i> lines;
  HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10 );
  for( size_t i = 0; i < lines.size(); i++ )
  {
    Vec4i l = lines[i];
    line( cdst, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0,0,255), 3, CV_AA);
  }
 #endif
 imshow("source", src);
 imshow("detected lines", cdst);

 waitKey();

 return 0;
}