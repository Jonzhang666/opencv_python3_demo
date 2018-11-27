import cv2 as cv
import numpy as np

def edge_image(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("canny边缘", edge_output)
    return edge_output

#轮廓发现
def contours_image(image):
    '''dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("二值化", binary)'''
    binary = edge_image(image)
    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 1)
    cv.imshow("轮廓", image)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)
        print(i)
    cv.imshow("轮廓覆盖", image)


src = cv.imread("coins.jpg")
cv.imshow("原来", src)
contours_image(src)
cv.waitKey(0)
cv.destroyAllWindows()