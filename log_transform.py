"""
Applies a log intensity transform to compress a wide dynamic range
(brightens dark regions, compresses bright ones), then displays the
grayscale original and transformed image side by side.

Requires: input_image.jpg in the working directory.
"""
import cv2
import numpy as np

img = cv2.imread("input_image.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

C = 20  # scaling constant
log_img = C * np.log(1 + gray_img.astype(np.float64))
log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

result = cv2.hconcat([gray_img, log_img])
cv2.imshow("Log transformation", result)
cv2.imwrite("log_transform_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
