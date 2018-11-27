import cv2 as cv
import numpy as np


def erode_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)

def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.dilate(binary, kernel)
    cv.imshow("erode_demo", dst)



src = cv.imread("1.jpg")
cv.imshow("original", src)
dilate_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
