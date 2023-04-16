## to watch camera image locally
import cv2
# open camera
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
#print(cap.isOpened())
# set dimensions
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
if not cap.isOpened():
    print("cannot open the camera")

while True:
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(10) & 0xff==27:
        cv2.destroyAllWindows()
 #   cap.release()
  #  cv2.destroyAllWindows()
