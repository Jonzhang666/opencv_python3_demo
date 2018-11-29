import cv2 as cv
import numpy as np

def face_detection_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("E:/python-3.6.6-64-bit/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 5)  # 第二个参数是移动距离，第三个参数是识别度，越大识别读越高
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 后两个参数，一个是颜色，一个是边框宽度
    cv.imshow("result", image)

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
        cv.imshow("original", frame)

        face_detection_demo(frame)
        # 设置视频刷新频率，单位为毫秒
        # 返回值为键盘按键的值
        c = cv.waitKey(50)

        # 27为 Esc 按键的返回值
        if c == 27:
            break

'''
src = cv.imread("face.jpg")
cv.namedWindow('original', cv.WINDOW_AUTOSIZE)
cv.namedWindow('result', cv.WINDOW_AUTOSIZE)
cv.imshow("original", src)
face_detection_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
'''

cv.namedWindow('original', cv.WINDOW_AUTOSIZE)
cv.namedWindow('result', cv.WINDOW_AUTOSIZE)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
