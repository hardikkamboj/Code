import cv2
import sys
import numpy

PREVIEW  = 0  # Preview Mode
BLUR     = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY    = 3  # Canny Edge Detector

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)
s = 0

image_filter = PREVIEW
alive = True

win_name = "Camera Filters"
win_name2 = "Blurred"

cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.namedWindow(win_name2, cv2.WINDOW_NORMAL)

result = None
result2 = None

source = cv2.VideoCapture(s)

frame_width = int(source.get(3))
frame_height = int(source.get(4))
fontScale = 2
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (255, 255, 255)
fontThickness = 2


LT = 140
UT = 150

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)


    frame1 = frame.copy()
    
    if image_filter == PREVIEW:
        result1 = frame1
    elif image_filter == CANNY:

        result1 = cv2.Canny(frame1, LT, UT)

        cv2.putText(result1, f"L: {LT}", (50, 50), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
        cv2.putText(result1, f"U: {UT}", (50,100), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)

    elif image_filter == BLUR:
        result1 = cv2.blur(frame1, (13, 13))

    elif image_filter == FEATURES:
        result1 = frame1
        frame_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x, y in numpy.float32(corners).reshape(-1, 2):
                cv2.circle(result1, (int(x), int(y)), 10, (0, 255, 0), 1)

    cv2.imshow(win_name, result1)

    frame2 = frame.copy()
    if image_filter == PREVIEW:
        result2 = frame2
    elif image_filter == CANNY:

        result2 = cv2.blur(frame2, (3, 3))
        result2 = cv2.Canny(result2, LT, UT)

        # result2 = cv2.Canny(frame, LT, UT)

        # cv2.putText(result, f"L: {LT}", (int(frame_width/2), int(frame_height/2)), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
        # cv2.putText(result, f"U: {UT}", (int(frame_width/2), int(frame_height/2)+50), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)

        cv2.putText(result2, f"L: {LT}", (50, 50), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
        cv2.putText(result2, f"U: {UT}", (50,100), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)

    elif image_filter == BLUR:
        # result2 = cv2.blur(frame, (13, 13))
        result2 = cv2.blur(frame2, (3, 3))

    elif image_filter == FEATURES:
        result2 = frame2
        wasabi = frame2.copy()
        frame_gray2 = cv2.cvtColor(wasabi, cv2.COLOR_BGR2GRAY)
        corners2 = cv2.goodFeaturesToTrack(frame_gray2, **feature_params)
        if corners2 is not None:
            for a, b in numpy.float32(corners2).reshape(-1, 2):
                cv2.circle(result2, (int(a), int(b)), 10, (0, 255, 0), 1)

    cv2.imshow(win_name2, result2)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        alive = False
    elif key == ord("C") or key == ord("c"):
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):
        image_filter = BLUR
    elif key == ord("F") or key == ord("f"):
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"):
        image_filter = PREVIEW
    elif key == ord("A") or key == ord("a"):
        if (UT - LT > 6):
            LT = LT+5
    elif key == ord("Z") or key == ord("z"):
        if (LT > 5):
            LT = LT-5
    elif key == ord("S") or key == ord("s"):
        if (UT < 500):
            UT = UT+5
    elif key == ord("X") or key == ord("x"):
        if (UT - LT > 6):
            UT = UT-5

source.release()
cv2.destroyWindow(win_name)
cv2.destroyWindow(win_name2)
