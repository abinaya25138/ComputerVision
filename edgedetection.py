import cv2 
# read input image 
img = cv2.imread('input.jpg') 
# convert image to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# apply Gaussian blur to remove noise 
blur = cv2.GaussianBlur(gray, (5,5), 0) 
# apply Sobel operator to detect edges in x and y directions 
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3) 
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3) 
# combine edges detected in x and y directions 
edges = cv2.bitwise_or(sobelx, sobely) 
# apply non-maximum suppression to thin out edges 
edges = cv2.Canny(edges, 100, 200) 
# display original image and edge-detected image 
cv2.imshow('Original Image', img) 
cv2.imshow('Edge-Detected Image', edges) 
# save edge-detected image 
cv2.imwrite('output.jpg', edges) 
# wait for user to close the window 
cv2.waitKey(0) 
# close all windows
cv2.destroyAllWindows()
