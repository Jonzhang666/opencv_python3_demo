import cv2 as cv
import numpy as np


# 图像的开闭操作
def watershed_demo(image):
    print(image.shape)
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)
    # gray\binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2) # two tomes
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("morphology operation", sure_bg)

    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance-t", dist_output*40)

    # markers
    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(image, markers=markers)
    image[markers == -1] = [0, 0, 255]
    cv.imshow("result", image)


src = cv.imread("02.png")
cv.imshow("original", src)
watershed_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()