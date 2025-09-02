import cv2
img=cv2.imread("/home/newuser/Pictures/Webcam/immg.jpg")
# cap=cv2.VideoCapture(0)
# ret,frame=cap.read()
# frame=cv2.flip(frame,1)
# cv2.imwrite(img,frame)
# cap.release()
# cv2.destroyAllWindows()
cap=cv2.VideoCapture(0)
show_img=False
alpha=0
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    if  img is not None:
        img_resized=cv2.resize(img,(frame.shape[1],frame.shape[0]))
    else:
        img_resized=frame
    if show_img and alpha < 1:
        alpha += 0.01
    if not show_img and alpha > 0:
        alpha -= 0.01   
    blended = cv2.addWeighted(img_resized, alpha, frame, 1 - alpha, 0)
    cv2.imshow("frame",blended)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        show_img=True
    if key == ord("v"):
        show_img=False
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
