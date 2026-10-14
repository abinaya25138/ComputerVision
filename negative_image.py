"""
Computes the photographic negative of an image's grayscale version.
Press 's' to save the negative while the window is focused.

Requires: input_image.jpg in the working directory.
"""
import cv2

img = cv2.imread("input_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
negative = cv2.bitwise_not(gray)

cv2.imshow("Input Image", img)
cv2.imshow("Negative Image", negative)

key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("negative_image.jpg", negative)

cv2.destroyAllWindows()
