import cv2 as cv
import numpy as np

# 边缘检测述算法
def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshold value : %s"%ret)
    cv.imshow("binary image", binary)
    outImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h) / max(w, h)
        print("rectangle rate : %s"%rate)
        mm = cv.moments(contour)
        print(type(mm))
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        #cv.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area : %s" %area)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] == 4:
            cv.drawContours(image, contours, i, (0, 255, 0), 5)
        if approxCurve.shape[0] == 8:
            cv.drawContours(image, contours, i, (0, 0, 255), 5)
        if approxCurve.shape[0] == 5:
            cv.drawContours(image, contours, i, (255, 0, 0), 5)
    cv.imshow("measure-contours", image)


src = cv.imread("shape.jpg")
cv.imshow("原来", src)
measure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()