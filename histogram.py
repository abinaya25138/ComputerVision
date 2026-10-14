"""
Loads an image, plots its grayscale intensity histogram two ways
(cv2.calcHist and numpy's ravel + matplotlib), then applies histogram
equalization to improve contrast.

Requires: input_image.jpg in the working directory.
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input_image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.title("Original")
plt.imshow(img)

img_hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.subplot(222)
plt.title("Histogram (cv2.calcHist)")
plt.plot(img_hist)

plt.subplot(223)
plt.hist(img_gray.ravel(), 256, [0, 256])
plt.title("Histogram (numpy ravel)")

# Histogram equalization must run on a single-channel (grayscale) image
final_image = cv2.equalizeHist(img_gray)
plt.subplot(224)
plt.title("Histogram Equalization")
plt.imshow(final_image, cmap="gray")

plt.show()
