import cv2 as cv
import numpy as np


def mo_image(src1):
    src2 = cv.blur(src1, (5, 5))
    cv.imshow("均值模糊", src2)

    src2 = cv.medianBlur(src1, 5)
    cv.imshow("中值模糊", src2)

    src2 = cv.GaussianBlur(src1, (5, 5), 2)
    cv.imshow("高斯模糊", src2)

    src2 = cv.bilateralFilter(src1, 5, 5, 2)
    cv.imshow("双边滤波", src2)


# 自定义模糊函数
def zi_image(src1):
    kernel1 = np.ones((5, 5), np.float)/25  # 自定义矩阵，并防止数值溢出
    src2 = cv.filter2D(src1, -1, kernel1)
    cv.imshow("自定义均值模糊", src2)
    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    src2 = cv.filter2D(src1, -1, kernel2)
    cv.imshow("自定义锐化", src2)

src = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)
zi_image(src)
mo_image(src)
cv.waitKey(0)
cv.destroyAllWindows()