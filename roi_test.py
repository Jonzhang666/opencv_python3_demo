#导入cv模块
import numpy as np
import cv2 as cv

# 截取图片中的指定区域或在指定区域添加某一图片
def jie_image(src1):
    src2 = src1[5:89, 500:630]  # 截取第5行到89行的第500列到630列的区域
    cv.imshow("cut", src2)
    src1[105:189, 300:430] = src2   # 指定位置填充，大小要一样才能填充
    cv.imshow("connect", src1)

# 指定颜色填充
def fill_image(image):
    copyImage = image.copy()    # 复制原图像
    h, w = image.shape[:2]  # 读取图像的宽和高
    mask = np.zeros([h+2, w+2], np.uint8)# 新建图像矩阵  +2是官方函数要求
    cv.floodFill(copyImage, mask, (0, 10), (0, 100, 255), (100, 100, 50), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill1", copyImage)

    mask = np.ones([h+2, w+2, 1], np.uint8) # 新建图像矩阵  +2是官方函数要求
    mask[101:301, 101:301] = 0
    cv.floodFill(copyImage, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill2", copyImage)


#指定位置填充
def fill2_image():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("origin", image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (100, 100), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill3", image)


src = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
cv.namedWindow('Image',cv.WINDOW_NORMAL)
cv.imshow('Image',src)
#jie_image(src)
#fill_image(src)
fill2_image()
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()