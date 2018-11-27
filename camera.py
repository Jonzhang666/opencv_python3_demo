import cv2 as cv


def video_demo():
    # 打开0号摄像头，捕捉该摄像头实时信息
    # 参数0代表摄像头的编号
    # 有多个摄像头的情况下，可用编号打开摄像头
    # 若是加载视频，则将参数改为视频路径，cv.VideoCapture加载视频是没有声音的，OpenCV只对视频的每一帧进行分析
    capture = cv.VideoCapture(0)
    while (True):
        # 获取视频的返回值 ref 和视频中的每一帧 frame
        ref, frame = capture.read()

        # 加入该段代码将使拍出来的画面呈现镜像效果
        # 第二个参数为视频是否上下颠倒 0为上下颠倒 1为不进行上下颠倒
        frame = cv.flip(frame, 1)

        # 将每一帧在窗口中显示出来
        cv.imshow("video", frame)

        # 设置视频刷新频率，单位为毫秒
        # 返回值为键盘按键的值
        c = cv.waitKey(50)

        # 27为 Esc 按键的返回值
        if c == 27:
            break


def get_image_info(image):
    # 图像类别
    # 图像类别为numpy.dnarray,即n维数组
    print(type(image))

    # 获取图像通道数目
    # 返回值如：(900, 640, 3)
    # 这三个数字代表图片纵向像素、横向像素和通道数目
    print(image.shape)

    # 图像总大小，计算公式为：长*宽*通道数目
    print(image.size)

    # 每个像素点所占字节位数
    print(image.dtype)


# 读入图片文件
src = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
get_image_info(src)
# 将图片保存为 testSave.png
cv.imwrite("testSave.png", src)
video_demo()
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()
