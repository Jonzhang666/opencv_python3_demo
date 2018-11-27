import cv2 as cv
import numpy as np


def top_hat_gray_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    #cimage = np.array(gray.shape, np.uint8)
    ciamge = 50;
    dst = cv.add(dst, ciamge)
    cv.imshow("top_hat", dst)

def black_hat_gray_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    #cimage = np.array(gray.shape, np.uint8)
    ciamge = 50;
    dst = cv.add(dst, ciamge)
    cv.imshow("top_hat", dst)

def hat_binary_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("top_hat", dst)

def graident_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    binary = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("close", binary)

def internal_external_graident_image(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em) # internal gradient
    dst2 = cv.subtract(dm, image)  # external gradient
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)


src = cv.imread("1.jpg")
cv.imshow("original", src)
internal_external_graident_image(src)
cv.waitKey(0)
cv.destroyAllWindows()