#导入cv模块
import numpy as np
import cv2 as cv


def ColorSpace(image):
    """
    色彩空间转化
    RGB转换为其他色彩空间
    """
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    cv.imshow("gray",gray)
    hsv=cv.cvtColor(image,cv.COLOR_RGB2HSV)
    cv.imshow("hsv",hsv)
    yuv=cv.cvtColor(image,cv.COLOR_RGB2YUV)
    cv.imshow("yuv",yuv)
    ycrcb=cv.cvtColor(image,cv.COLOR_RGB2YCrCb)
    cv.imshow("ycrcb",ycrcb)

def extrace_object_demo():
    capture=cv.VideoCapture(0)
    while(True):
        ret,frame=capture.read()
        frame = cv.flip(frame, 1)
        '''
        b,g,r = cv.split(frame)
        cv.imshow("blue",b)
        cv.imshow("green", g)
        cv.imshow("red", r)

        r = np.zeros(frame.shape[:2], dtype = "uint8")

        frame =cv.merge([b,g,r])
        frame[:,:,1] = 0
        cv.imshow("image after", frame)
        '''
        if ret==False:
            break;
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv=np.array([37,43,46])
        upperb_hsv = np.array([77, 255, 255])
        mask=cv.inRange(hsv,lowerb=lower_hsv,upperb=upperb_hsv)
        dst = cv.bitwise_and(frame,frame,mask=mask)

        cv.imshow("video_mask", frame)
        cv.imshow("video",dst)
        c=cv.waitKey(40)
        if c==27:
            break;


#src = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
#cv.namedWindow('Image',cv.WINDOW_NORMAL)
#cv.imshow('Image',src)
extrace_object_demo()

# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()