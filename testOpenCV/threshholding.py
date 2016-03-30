# import numpy as np
# import cv2

# cap = cv2.VideoCapture("output.avi")

# while(cap.isOpened()):
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import numpy as np
# import cv2

# cap = cv2.VideoCapture("http://192.168.1.10:8080/stream?topic=/image&dummy=param.mjpg")

# # Define the codec and create VideoWriter object
# fourcc = cv2.cv.CV_FOURCC(*'MJPG')
# out = cv2.VideoWriter('output3.avi',fourcc, 20.0, (640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)

#         # write the flipped frame
#         out.write(frame)

#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread("http://192.168.1.10:8080/stream?topic=/image&dummy=param.mjpg",0)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
 
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#      plt.title(titles[i])
#      plt.xticks([]),plt.yticks([])
 
# plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture("http://192.168.1.10:8080/stream?topic=/image&dummy=param.mjpg")

while True:
    if cap.grab():
        flag, frame = cap.retrieve()
        if not flag:
            continue
        else:
			ret,thresh1 = cv2.threshold(frame,127,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
   10             cv2.THRESH_BINARY,11,2)
			cv2.imshow('thresh1', thresh1)
    if cv2.waitKey(10) == 27:
        break