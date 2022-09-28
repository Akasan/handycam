from handycam import HandyVideoCapture
import cv2


# Open video capture of web camera which id is 0 and read frames
with HandyVideoCapture(0) as cap:
    for frame in cap.reads(3):
        cv2.imshow("hoge", frame)
        if cv2.waitKey(20) == ord("q"):
            cv2.destroyAllWindows()
            break