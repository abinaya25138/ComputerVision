import numpy as np 
import cv2 
# Define the size of the calibration pattern 
pattern_size = (7, 6) # number of interior corners on each row and column 
# Define the coordinates of the calibration pattern corners in the calibration pattern coordinate system 
objp = np.zeros((pattern_size[0]*pattern_size[1], 3), np.float32) 
objp[:,:2] = np.mgrid[0:pattern_size[0],0:pattern_size[1]].T.reshape(-1,2) * 30 # assume square size of 30mm 
# Capture several images of the calibration pattern from different angles 
images = [] # list of images 
while True: 
ret, img = cap.read() # capture an image from the camera 
if not ret: 
break 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)
if ret: 
cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)) 
images.append((img, corners)) 
# Compute the camera calibration parameters 
objpoints = [] # list of object points for each image 
imgpoints = [] # list of image points for each image 
for img, corners in images: 
objpoints.append(objp) 
imgpoints.append(corners) 
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None) 
# Compute the reprojection error 
mean_error = 0 
for i in range(len(objpoints)): 
imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist) 
error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2) 
mean_error += error 
print("Mean reprojection error: ", mean_error/len(objpoints)) 
# Use the obtained calibration parameters to undistort an image 
img = cv2.imread("test.jpg") 
undistorted = cv2.undistort(img, mtx, dist) 
cv2.imshow("Undistorted image", undistorted) 
cv2.waitKey(0)
