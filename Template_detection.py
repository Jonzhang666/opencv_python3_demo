#导入cv模块
import numpy as np
import cv2 as cv

def template_image():
    tpl = cv.imread("2.png")
    target = cv.imread("1.jpg")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow("Æ¥Åä"+np.str(md), target)





src = cv.imread("D:/pythonworkplace/opencv_test/test.jpg")
cv.namedWindow('Image',cv.WINDOW_NORMAL)
cv.imshow('Image',src)
#jie_image(src)
#fill_image(src)
template_image()
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()