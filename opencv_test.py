#导入cv模块
import numpy as np
import cv2 as cv


# 输出图片属性
def get_image_info(image):  # 定义一个函数来输出图片的一些属性
    print(type(image))  # 显示图片类型 numpy类型的数组
# 图像矩阵的shape属性表示图像的大小，shape会返回tuple元组，第一个元素表示矩阵行数，第二个元组表示矩阵列数，第三个元素是3，表示像素值由光的三原色组成
    print(image.shape)
    print(image.size)   # 图像大小
    print(image.dtype)  # 图像类型
    pixel_data = np.array(image)
    print(pixel_data)   # 图片矩阵


#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("D:/pythonworkplace/opencv_test/test.jpg",cv.IMREAD_COLOR)
#创建窗口并显示图像
cv.namedWindow('Image',cv.WINDOW_NORMAL)
cv.imshow('Image',img)
get_image_info(img)
k = cv.waitKey(0)
#释放窗口
if k==27:
    cv.destroyAllWindows()  #wait for ESC key to exit
elif k == ord('s'):
    cv.imwrite("46.png", img)  #wait for 's' key to save and exit
    cv.waitKey(0)&0xFF
    cv.destoryAllWindows()


from matplotlib import pyplot as plt
img =cv.imread('46.png',0)
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])  #to hide tick values on X and Y axis
plt.show()

