"""
Compares two edge-detection approaches on the same image: a Sobel-gradient
magnitude map, and the Canny edge detector.

Requires: input.jpg in the working directory.
"""
import cv2
import numpy as np

img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# --- Sobel: gradient magnitude in x and y, combined and normalized to 8-bit ---
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel_magnitude = cv2.magnitude(sobelx, sobely)
sobel_edges = cv2.convertScaleAbs(sobel_magnitude)

# --- Canny: non-maximum suppression + hysteresis thresholding ---
canny_edges = cv2.Canny(blur, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel Edges", sobel_edges)
cv2.imshow("Canny Edges", canny_edges)

cv2.imwrite("output_sobel.jpg", sobel_edges)
cv2.imwrite("output_canny.jpg", canny_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
