import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Flip the Image:
    frame = cv2.flip(frame, +1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()