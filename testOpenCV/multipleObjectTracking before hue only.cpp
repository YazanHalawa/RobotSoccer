//objectTrackingTutorial.cpp

//Written by  Kyle Hounslow 2013

//Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software")
//, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
//and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

//The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
//LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
//IN THE SOFTWARE.

#include <sstream>
#include <string>
#include <iostream>
#include "opencv2/highgui/highgui.hpp"
#include "opencv/cv.hpp"
#include "std_msgs/String.h"

//opencv
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/video/background_segm.hpp>
//#include "/usr/include/opencv2/highgui/highgui.hpp"
//#include "/usr/include/opencv/cv.hpp"
//C
#include <stdio.h>
//C++
#include <cmath>

using namespace cv;
using namespace std;

//initial min and max HSV filter values.
//these will be changed using trackbars
int Center_X = 432;
int Center_Y = 240;

int BALL_H_MIN = 156;
int BALL_H_MAX = 221;
int BALL_S_MIN = 119;
int BALL_S_MAX = 186;
int BALL_V_MIN = 195;
int BALL_V_MAX = 256;

int BALL_X = 1;
int BALL_Y = 1;

int HOME_H_MIN = 65;
int HOME_H_MAX = 85;
int HOME_S_MIN = 60;
int HOME_S_MAX = 150;
int HOME_V_MIN = 0;
int HOME_V_MAX = 256;

int HOME_X = 1;
int HOME_Y = 1;
int HOME_THETA = 1;

int HOME2_H_MIN = 0;
int HOME2_H_MAX = 256;
int HOME2_S_MIN = 0;
int HOME2_S_MAX = 256;
int HOME2_V_MIN = 150;
int HOME2_V_MAX = 256;

int HOME2_X = 1;
int HOME2_Y = 1;
int HOME2_THETA = 1;

int AWAY_H_MIN = 0;
int AWAY_H_MAX = 256;
int AWAY_S_MIN = 0;
int AWAY_S_MAX = 256;
int AWAY_V_MIN = 0;
int AWAY_V_MAX = 256;

int AWAY_X = 1;
int AWAY_Y = 1;
int AWAY_THETA = 1;

int AWAY2_H_MIN = 0;
int AWAY2_H_MAX = 256;
int AWAY2_S_MIN = 0;
int AWAY2_S_MAX = 256;
int AWAY2_V_MIN = 0;
int AWAY2_V_MAX = 256;

int AWAY2_X = 1;
int AWAY2_Y = 1;
int AWAY2_THETA = 1;

int TEST_THETA = 1;
int TEST_THETA_MIN = 0;
int TEST_THETA_MAX = 2*314;

//default capture width and height
const int FRAME_WIDTH = 840;
const int FRAME_HEIGHT = 480;


const int MAX_NUM_OBJECTS=50;

//minimum and maximum object area
//const int MIN_OBJECT_AREA = 4*4;
const double MAX_OBJECT_AREA = 25*25;

//minimum and maximum object distances
//const int MIN_OBJECT_DIST = 5;
const int MAX_OBJECT_DIST = 30;

//names that will appear at the top of each window
const string windowName = "Field";
const string trackbarWindowName = "Trackbars";

typedef struct {
	string w_name = "";
	int x;
	int y;
	double theta;
} Positions;

Positions ball_pos;
Positions home_pos;
Positions home2_pos;
Positions away_pos;
Positions away2_pos;

void on_trackbar( int, void* )
{//This function gets called whenever a trackbar position is changed

Center_X = getTrackbarPos( "Center_X", trackbarWindowName);
Center_Y = getTrackbarPos( "Center_Y", trackbarWindowName);

TEST_THETA = getTrackbarPos( "TEST_THETA", trackbarWindowName);

BALL_H_MIN = getTrackbarPos( "BALL_H_MIN", trackbarWindowName);
BALL_H_MAX = getTrackbarPos( "BALL_H_MAX", trackbarWindowName);
BALL_S_MIN = getTrackbarPos( "BALL_S_MIN", trackbarWindowName);
BALL_S_MAX = getTrackbarPos( "BALL_S_MAX", trackbarWindowName);
BALL_V_MIN = getTrackbarPos( "BALL_V_MIN", trackbarWindowName);
BALL_V_MAX = getTrackbarPos( "BALL_V_MAX", trackbarWindowName);

HOME_H_MIN = getTrackbarPos( "HOME_H_MIN", trackbarWindowName);
HOME_H_MAX = getTrackbarPos( "HOME_H_MAX", trackbarWindowName);
HOME_S_MIN = getTrackbarPos( "HOME_S_MIN", trackbarWindowName);
HOME_S_MAX = getTrackbarPos( "HOME_S_MAX", trackbarWindowName);
HOME_V_MIN = getTrackbarPos( "HOME_V_MIN", trackbarWindowName);
HOME_V_MAX = getTrackbarPos( "HOME_V_MAX", trackbarWindowName);
/*
HOME2_H_MIN = getTrackbarPos( "HOME2_H_MIN", trackbarWindowName);
HOME2_H_MAX = getTrackbarPos( "HOME2_H_MAX", trackbarWindowName);
HOME2_S_MIN = getTrackbarPos( "HOME2_S_MIN", trackbarWindowName);
HOME2_S_MAX = getTrackbarPos( "HOME2_S_MAX", trackbarWindowName);
HOME2_V_MIN = getTrackbarPos( "HOME2_V_MIN", trackbarWindowName);
HOME2_V_MAX = getTrackbarPos( "HOME2_V_MAX", trackbarWindowName);

AWAY_H_MIN = getTrackbarPos( "AWAY_H_MIN", trackbarWindowName);
AWAY_H_MAX = getTrackbarPos( "AWAY_H_MAX", trackbarWindowName);
AWAY_S_MIN = getTrackbarPos( "AWAY_S_MIN", trackbarWindowName);
AWAY_S_MAX = getTrackbarPos( "AWAY_S_MAX", trackbarWindowName);
AWAY_V_MIN = getTrackbarPos( "AWAY_V_MIN", trackbarWindowName);
AWAY_V_MAX = getTrackbarPos( "AWAY_V_MAX", trackbarWindowName);

AWAY2_H_MIN = getTrackbarPos( "AWAY2_H_MIN", trackbarWindowName);
AWAY2_H_MAX = getTrackbarPos( "AWAY2_H_MAX", trackbarWindowName);
AWAY2_S_MIN = getTrackbarPos( "AWAY2_S_MIN", trackbarWindowName);
AWAY2_S_MAX = getTrackbarPos( "AWAY2_S_MAX", trackbarWindowName);
AWAY2_V_MIN = getTrackbarPos( "AWAY2_V_MIN", trackbarWindowName);
AWAY2_V_MAX = getTrackbarPos( "AWAY2_V_MAX", trackbarWindowName);
*/
}
string intToString(int number){

	std::stringstream ss;
	ss << number;
	return ss.str();
}
string dblToString(double dbl){

	std::ostringstream strs;
	strs << dbl;
	return strs.str();
}
int cartesian_x(int x){
	return x - Center_X;
}
int cartesian_y(int y){
	return Center_Y - y;
}
int image_x(int cartesian_x){
	return cartesian_x + Center_X;
}
int image_y(int cartesian_y){
	return Center_Y + cartesian_y;
}
void createTrackbars(){
	//create window for trackbars
	namedWindow(trackbarWindowName,0);

	//create trackbars and insert them into window
	//3 parameters are: the address of the variable that is changing when the trackbar is moved(eg.H_LOW),
	//the max value the trackbar can move (eg. H_HIGH), 
	//and the function that is called whenever the trackbar is moved(eg. on_trackbar)        

	createTrackbar( "Center_X", trackbarWindowName, &Center_X, FRAME_WIDTH, on_trackbar );
	createTrackbar( "Center_Y", trackbarWindowName, &Center_Y, FRAME_HEIGHT, on_trackbar );

	createTrackbar( "TEST_THETA", trackbarWindowName, &TEST_THETA_MIN, TEST_THETA_MAX, on_trackbar );

	createTrackbar( "BALL_H_MIN", trackbarWindowName, &BALL_H_MIN, 256, on_trackbar );
	createTrackbar( "BALL_H_MAX", trackbarWindowName, &BALL_H_MAX, 256, on_trackbar );
	createTrackbar( "BALL_S_MIN", trackbarWindowName, &BALL_S_MIN, 256, on_trackbar );
	createTrackbar( "BALL_S_MAX", trackbarWindowName, &BALL_S_MAX, 256, on_trackbar );
	createTrackbar( "BALL_V_MIN", trackbarWindowName, &BALL_V_MIN, 256, on_trackbar );
	createTrackbar( "BALL_V_MAX", trackbarWindowName, &BALL_V_MAX, 256, on_trackbar );

	createTrackbar( "HOME_H_MIN", trackbarWindowName, &HOME_H_MIN, 256, on_trackbar );
	createTrackbar( "HOME_H_MAX", trackbarWindowName, &HOME_H_MAX, 256, on_trackbar );
	createTrackbar( "HOME_S_MIN", trackbarWindowName, &HOME_S_MIN, 256, on_trackbar );
	createTrackbar( "HOME_S_MAX", trackbarWindowName, &HOME_S_MAX, 256, on_trackbar );
	createTrackbar( "HOME_V_MIN", trackbarWindowName, &HOME_V_MIN, 256, on_trackbar );
	createTrackbar( "HOME_V_MAX", trackbarWindowName, &HOME_V_MAX, 256, on_trackbar );
/*
	createTrackbar( "HOME2_H_MIN", trackbarWindowName, &HOME2_H_MIN, 256, on_trackbar );
	createTrackbar( "HOME2_H_MAX", trackbarWindowName, &HOME2_H_MAX, 256, on_trackbar );
	createTrackbar( "HOME2_S_MIN", trackbarWindowName, &HOME2_S_MIN, 256, on_trackbar );
	createTrackbar( "HOME2_S_MAX", trackbarWindowName, &HOME2_S_MAX, 256, on_trackbar );
	createTrackbar( "HOME2_V_MIN", trackbarWindowName, &HOME2_V_MIN, 256, on_trackbar );
	createTrackbar( "HOME2_V_MAX", trackbarWindowName, &HOME2_V_MAX, 256, on_trackbar );

	createTrackbar( "AWAY_H_MIN", trackbarWindowName, &AWAY_H_MIN, 256, on_trackbar );
	createTrackbar( "AWAY_H_MAX", trackbarWindowName, &AWAY_H_MAX, 256, on_trackbar );
	createTrackbar( "AWAY_S_MIN", trackbarWindowName, &AWAY_S_MIN, 256, on_trackbar );
	createTrackbar( "AWAY_S_MAX", trackbarWindowName, &AWAY_S_MAX, 256, on_trackbar );
	createTrackbar( "AWAY_V_MIN", trackbarWindowName, &AWAY_V_MIN, 256, on_trackbar );
	createTrackbar( "AWAY_V_MAX", trackbarWindowName, &AWAY_V_MAX, 256, on_trackbar );

	createTrackbar( "AWAY2_H_MIN", trackbarWindowName, &AWAY2_H_MIN, 256, on_trackbar );
	createTrackbar( "AWAY2_H_MAX", trackbarWindowName, &AWAY2_H_MAX, 256, on_trackbar );
	createTrackbar( "AWAY2_S_MIN", trackbarWindowName, &AWAY2_S_MIN, 256, on_trackbar );
	createTrackbar( "AWAY2_S_MAX", trackbarWindowName, &AWAY2_S_MAX, 256, on_trackbar );
	createTrackbar( "AWAY2_V_MIN", trackbarWindowName, &AWAY2_V_MIN, 256, on_trackbar );
	createTrackbar( "AWAY2_V_MAX", trackbarWindowName, &AWAY2_V_MAX, 256, on_trackbar );
*/

}
void drawObject(int x,int y,Mat &frame){

	cv::circle(frame,cv::Point(x,y),10,cv::Scalar(0,0,255));
	cv::putText(frame,intToString(cartesian_x(x))+ " , " + intToString(cartesian_y(y)),cv::Point(x,y+20),1,1,Scalar(0,255,0));

}
void drawAngle(Mat &frame, int x, int y, double angle_rads){

	int x2 = 20*cos(angle_rads)+x;
	int y2 = (-20*sin(angle_rads))+y;//minus instead of plus because of the image pixel numbering

	line(frame, cv::Point(x,y), cv::Point(x2,y2), cv::Scalar(0,0,255));
	cv::putText(frame, intToString(cartesian_x(x)),cv::Point((x+10),y),1,1,Scalar(0,255,0));
	cv::putText(frame, intToString(cartesian_y(y)),cv::Point((x+10),(y+10)),1,1,Scalar(0,255,0));
	cv::putText(frame, dblToString(angle_rads),cv::Point((x+10),(y+20)),1,1,Scalar(0,255,0));

}
void drawCenter(Mat &frame){

	cv::putText(frame,intToString(Center_X)+ " , " + intToString(Center_Y),cv::Point(Center_X+10,Center_Y-20),1,1,Scalar(0,255,0));
	line(frame, cv::Point(Center_X-20,Center_Y), cv::Point(Center_X+20,Center_Y), cv::Scalar(0,0,255));
	line(frame, cv::Point(Center_X,Center_Y-20), cv::Point(Center_X,Center_Y+20), cv::Scalar(0,0,255));

	//TEST ANGLE - Comment out the lower two lines when not testing Theta
	//drawAngle(frame, Center_X, Center_Y, TEST_THETA/100.0);
	//cv::putText(frame,"TEST Angle (Rads) : " + dblToString(TEST_THETA),cv::Point(Center_X+10,Center_Y-50),1,1,Scalar(0,255,0));

}
void morphOps(Mat &thresh){

	Mat erodeElement = getStructuringElement( MORPH_RECT,Size(2,2));
	Mat dilateElement = getStructuringElement( MORPH_RECT,Size(6,6));

	erode(thresh,thresh,erodeElement);
	dilate(thresh,thresh,dilateElement);

}
double findAngle(int smallX, int largeX, int smallY, int largeY){//X,Y of large mass, XY of smaller Mass

	return (double)atan2((double)(largeY-smallY), (double)(smallX-largeX));
}
void trackObject(Positions &p, Mat threshold, int Hmin, int Smin, int Vmin, int Hmax, int Smax, int Vmax ){

	inRange(threshold,Scalar(Hmin,Smin,Vmin),Scalar(Hmax,Smax,Vmax),threshold);
	morphOps(threshold);

	Mat temp;
	threshold.copyTo(temp);
	//these two vectors needed for output of findContours
	vector< vector<Point> > contours;
	vector<Vec4i> hierarchy;
	//find contours of filtered image using openCV findContours function
	findContours(temp,contours,hierarchy,CV_RETR_CCOMP,CV_CHAIN_APPROX_SIMPLE );
	//use moments method to find our filtered object
	int index_largest = -1;
	int index_second_largest = -1;

	double area_largest = 0;
	double area_second_largest = 0;

	double refArea = 0;
	bool objectFound = false;
	if (hierarchy.size() > 0) {
		int numObjects = hierarchy.size();
		//if number of objects greater than MAX_NUM_OBJECTS we have a noisy filter
		if(numObjects<MAX_NUM_OBJECTS){
			for (int index = 0; index >= 0; index = hierarchy[index][0]) {

				Moments moment = moments((cv::Mat)contours[index]);
				double area = moment.m00;

				if(area < MAX_OBJECT_AREA){
					if(area > area_largest){
						area_second_largest = area_largest;
						index_second_largest = index_largest;
						area_largest = area;
						index_largest = index;
					}
					else if(area > area_second_largest){
						area_second_largest = area;
						index_second_largest = index;
					}
				}
			}
			//let user know you found an object
			if(index_second_largest > -1 && index_largest > -1){

				//draw object location on screen
				int largeX,largeY, smallX, smallY;

				Moments moment = moments((cv::Mat)contours[index_largest]);
				double area = moment.m00;
				largeX = moments((cv::Mat)contours[index_largest]).m10/area;
				largeY = moments((cv::Mat)contours[index_largest]).m01/area;

				moment = moments((cv::Mat)contours[index_second_largest]);
				area = moment.m00;
				smallX = moments((cv::Mat)contours[index_second_largest]).m10/area;
				smallY = moments((cv::Mat)contours[index_second_largest]).m01/area;				

				int xdist = abs(largeX-smallX);
				int ydist = abs(largeY-smallY);

				if(xdist < MAX_OBJECT_DIST && ydist < MAX_OBJECT_DIST){
					p.x = (largeX+smallX)/2;
					p.y = (largeY+smallY)/2;
					p.theta = findAngle(smallX, largeX, smallY, largeY);
				}
			}
			else if(index_largest > -1 && p.w_name == "Ball config"){
				Moments moment = moments((cv::Mat)contours[index_largest]);
				double area = moment.m00;
				p.x = moments((cv::Mat)contours[index_largest]).m10/area;
				p.y = moments((cv::Mat)contours[index_largest]).m01/area;
			}

		}//imshow(p.w_name,threshold);
	}
}

int main(int argc, char* argv[])
{
	//if we would like to calibrate our filter values, set to true.
	bool calibrationMode = true;
	
	//Matrix to store each frame of the webcam feed
	Mat cameraFeed;
	Mat dst;               // dst must be a different Mat

	Mat fgMaskMOG2; //fg mask fg mask generated by MOG2 method
	Ptr<BackgroundSubtractor> pMOG2; //MOG2 Background subtractor

	if(calibrationMode){
		//create slider bars for HSV filtering
		createTrackbars();
	}

    //create GUI windows
    //namedWindow("FG Mask MOG 2");
        //create Background Subtractor objects 
    pMOG2 = new BackgroundSubtractorMOG2(1000,25,false); //MOG2 approach (int history, float varThreshold, bool bShadowDetection=true )http://docs.opencv.org/2.4/modules/video/doc/motion_analysis_and_object_tracking.html?highlight=backgroundsubtractorMOG2#backgroundsubtractormog2


	//video capture object to acquire webcam feed
	VideoCapture capture;
	//capture.set(CV_CAP_PROP_MODE, CV_CAP_PROP_HUE);
	capture.open("http://192.168.1.78:8080/stream?topic=/image&dummy=param.mjpg");
	capture.set(CV_CAP_PROP_FRAME_WIDTH,FRAME_WIDTH);
	capture.set(CV_CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT);

	ball_pos.w_name = "Ball config";
	home_pos.w_name = "Home config";

	//start an infinite loop where webcam feed is copied to cameraFeed matrix
	//all of our operations will be performed within this loop
	while(1){

		//read the current frame
        if(!capture.read(cameraFeed)) {
            exit(EXIT_FAILURE);
        }
		Mat masked;
		//store image to matrix
		//capture.read(cameraFeed);
		cv::flip(cameraFeed, dst, -1); 


        //update the background model
        pMOG2->operator()(dst, fgMaskMOG2, .1);//(InputArray image, OutputArray fgmask, double learningRate=-1)

        Mat erodeElement = getStructuringElement(MORPH_RECT, Size(2, 2));
        erode(fgMaskMOG2, fgMaskMOG2, erodeElement);
        //dilate with larger element so make sure object is nicely visible
        Mat dilateElement = getStructuringElement(MORPH_RECT, Size(25, 25));
        dilate(fgMaskMOG2, fgMaskMOG2, dilateElement);

        //imshow("FG Mask MOG 2", fgMaskMOG2);

		//cvtColor(dst,dst,COLOR_BGR2HSV);
		
		//Mat chan[3];
		//split( dst, chan );
		//Mat H = chan[0];

		//bitwise_and(InputArray src1, InputArray src2, OutputArray dst, InputArray mask=noArray())
		//copyTo(chan[0], fgMaskMOG2, chan[0], fgMaskMOG2);


		dst.copyTo(masked, fgMaskMOG2);

		//merge(chan,3,dst);


        //imshow("Mask MOG 2", masked);

		//cvtColor(dst,HSV,COLOR_BGR2HSV);

		if(calibrationMode==true){

		}

		trackObject(ball_pos, masked, BALL_H_MIN, BALL_S_MIN, BALL_V_MIN, BALL_H_MAX, BALL_S_MAX, BALL_V_MAX );
		trackObject(home_pos, masked, HOME_H_MIN, HOME_S_MIN, HOME_V_MIN, HOME_H_MAX, HOME_S_MAX, HOME_V_MAX );
		trackObject(home2_pos, masked, HOME2_H_MIN, HOME2_S_MIN, HOME2_V_MIN, HOME2_H_MAX, HOME2_S_MAX, HOME2_V_MAX );
		trackObject(away_pos, masked, AWAY_H_MIN, AWAY_S_MIN, AWAY_V_MIN, AWAY_H_MAX, AWAY_S_MAX, AWAY_V_MAX );
		trackObject(away2_pos, masked, AWAY2_H_MIN, AWAY2_S_MIN, AWAY2_V_MIN, AWAY2_H_MAX, AWAY2_S_MAX, AWAY2_V_MAX );
		
		drawObject(ball_pos.x, ball_pos.y, dst);
		drawCenter(dst);
		
		cv::putText(dst,"Robot Info : " + intToString(home_pos.x) + " " + intToString(home_pos.y) ,cv::Point(Center_X+10,Center_Y-30),1,1,Scalar(0,255,0));
		drawAngle(dst, home_pos.x, home_pos.y, home_pos.theta);

		imshow(windowName,dst);

		std_msgs::String msg;

		std::stringstream ss;
		//ss << xpos << "," << ypos << "," << theta << endl;
		msg.data = ss.str();

		waitKey(1);
	}

	return 0;
}


