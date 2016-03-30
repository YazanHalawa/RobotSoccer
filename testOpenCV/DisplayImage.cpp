#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char** argv )
{
	cv::VideoCapture cap;
	//http://192.168.1.90/mjpg/video.mjpg
	//http://localhost:8080/stream_viewer?topic=/image
	cap.open("http://192.168.1.10:8080/stream?topic=/image&dummy=param.mjpg");
	if (!cap.isOpened())
	{
		printf("Not open!!\n");
		return 0;
	}
	while(true)
	{
		Mat img;
		cap.read(img);
		if(img.empty())
			break; // end of video stream
		imshow("Video", img);
		if(waitKey(1) == 27)
			break; //ESC
	}
	return 0;
}
