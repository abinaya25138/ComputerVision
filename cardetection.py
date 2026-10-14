"""
Car detection in video using a Haar cascade classifier.

Requires: cars.xml (a car Haar cascade - not bundled with OpenCV; several
are available from community cascade repositories) and video.avi in the
working directory.
"""
import cv2

haar_cascade = "cars.xml"
video = "video.avi"

cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars of different sizes in the frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("video", frame)

    # Wait for the Esc key to stop
    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()
