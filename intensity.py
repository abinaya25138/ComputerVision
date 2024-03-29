import cv2
# Load input image 
img = cv2.imread('input_image.jpg') 
# Convert input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# Compute negative of the grayscale image 
neg = cv2.bitwise_not(gray) 
# Display the input image and negative image 
cv2.imshow('Input Image', img) 
cv2.imshow('Negative Image', neg) 
# Wait for a key press 
key = cv2.waitKey(0) 
# If the key pressed is 's', save the negative image 
if key == ord('s'): 
cv2.imwrite('negative_image.jpg', neg) 
# Destroy all windows 
cv2.destroyAllWindows()

import cv2 
import numpy as np 
# Read input image 
img = cv2.imread('input_image.jpg') 
# Define gamma value for gamma correction 
gamma = 1.5 
# Define constant C for log transformation 
C = 20 
# Convert input image to grayscale 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# Perform log transformation 
log_img = C * np.log(1 + gray_img) 
# Display input and output images side by side 
result = cv2.hconcat([gray_img, log_img]) 
cv2.imshow(Log transformation', result) 
# Save the output image 
cv2.imwrite('output_image.jpg', result) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
