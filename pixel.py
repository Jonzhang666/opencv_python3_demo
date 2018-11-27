#导入cv模块
import numpy as np
import cv2 as cv

#数值运算：加减乘除
def shu_image(src11, src22):
    src = cv.add(src11, src22)#加
    cv.imshow("add", src)
    src = cv.subtract(src11, src22)#减
    cv.imshow("substract", src)
    src = cv.divide(src11, src22)#乘
    cv.imshow("divide", src)
    src = cv.multiply(src11, src22)#除
    cv.imshow("multiply", src)


#逻辑运算：与或非的操作
def luo_image(src11, src22):
    src = cv.bitwise_and(src11, src22)#与 两张图片同一位置的色素两个值均不为零的才会有输出
    cv.imshow("and", src)
    src = cv.bitwise_or(src11, src22)#或 两张图片同一位置的色素两个值不全为零的才会有输出
    cv.imshow("or", src)
    src = cv.bitwise_not(src11)#非 对一张图片操作  取反
    cv.imshow("not", src)
    src = cv.bitwise_xor(src11, src22)#异或 两张图片同一位置的色素两个值有一个为零，另一个不为零才会输出
    cv.imshow("xor", src)


# 粗略的调节对比度和亮度
def contrast_brightness_image(src1, a, g):
    h, w, ch = src1.shape  # 获取shape的数值，height和width、通道

    # 新建全零图片数组src2,将height和width，类型设置为原图片的通道类型(色素全为零，输出为全黑图片)
    src2 = np.zeros([h, w, ch], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1 - a, g)  # addWeighted函数说明如下
    cv.imshow("con-bri-demo", dst)

src1 = cv.imread("D:/pythonworkplace/opencv_test/linux.jpg")
src2 = cv.imread("D:/pythonworkplace/opencv_test/windows.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow('Image1',cv.WINDOW_NORMAL)
cv.imshow('Image1',src1)
cv.namedWindow('Image2',cv.WINDOW_NORMAL)
cv.imshow('Image2',src2)
shu_image(src1, src2)
luo_image(src1, src2)
src = contrast_brightness_image(src1, 1.5, 50)
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()