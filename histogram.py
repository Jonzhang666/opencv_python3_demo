#导入cv模块
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show()

#画出图像的直方图
def hist_image(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

#提升对比度（默认提升），只能是灰度图像
def equalHist_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("原   来", gray)
    dst = cv.equalizeHist(gray)
    cv.imshow("默认处理", dst)

#对比度限制（自定义提示参数）
def clahe_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    dst = clahe.apply(gray)
    cv.imshow("自定义处理", dst)

def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist

def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("bsjl: %s, xgx: %s, kf: %s"%(match1, match2, match3))

def back_projection_demo():
    sample = cv.imread("D:/pythonworkplace/opencv_test/sample.png")
    target = cv.imread("D:/pythonworkplace/opencv_test/target.png")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow('sample', sample)
    cv.imshow('target', target)

    roi_Hist = cv.calcHist([roi_hsv], [0,1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roi_Hist, roi_Hist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0,1], roi_Hist, [0, 180, 0, 256], 1)
    cv.imshow("BackProject", dst)

def his2d_demo(image):
    his = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([his], [0,1], None, [32, 32], [0, 180, 0, 256])
    plt.imshow(hist, interpolation='nearest')
    plt.title("2d histogram")
    plt.show()


'''
src1 = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
src2 = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
cv.namedWindow('Image1',cv.WINDOW_NORMAL)
cv.imshow('Image1',src1)
cv.namedWindow('Image2',cv.WINDOW_NORMAL)
cv.imshow('Image2',src2)
'''
src = cv.imread("D:/pythonworkplace/opencv_test/sample.png")
his2d_demo(src)
#hist_compare(src1, src2)
back_projection_demo()
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()