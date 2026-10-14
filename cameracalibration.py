"""
Camera calibration using a checkerboard pattern: captures several views of
a 7x6-corner checkerboard from a live camera, computes the camera matrix
and distortion coefficients, reports reprojection error, then undistorts
a test image.

Requires: a live camera (index 0), a printed 7x6 checkerboard, and test.jpg.
Press 'q' once you've captured enough calibration frames to move on.
"""
import cv2
import numpy as np

pattern_size = (7, 6)  # number of interior corners per row/column
square_size_mm = 30

# 3D coordinates of the checkerboard corners in the calibration pattern's own frame
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0 : pattern_size[0], 0 : pattern_size[1]].T.reshape(-1, 2) * square_size_mm

cap = cv2.VideoCapture(0)
images = []  # (frame, corners) pairs where the checkerboard was found

while True:
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, pattern_size, None)
    if found:
        corners = cv2.cornerSubPix(
            gray, corners, (11, 11), (-1, -1),
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001),
        )
        images.append((img, corners))
        cv2.drawChessboardCorners(img, pattern_size, corners, found)

    cv2.imshow("Calibration capture (press q when done)", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

if not images:
    raise RuntimeError("No checkerboard detected in any frame - try again with better lighting/angle.")

objpoints = [objp for _ in images]
imgpoints = [corners for _, corners in images]
gray_shape = cv2.cvtColor(images[0][0], cv2.COLOR_BGR2GRAY).shape[::-1]

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_shape, None, None)

mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error
print("Mean reprojection error:", mean_error / len(objpoints))

# Use the calibration to undistort a test image
img = cv2.imread("test.jpg")
if img is not None:
    undistorted = cv2.undistort(img, mtx, dist)
    cv2.imshow("Undistorted image", undistorted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
