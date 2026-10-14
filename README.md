# Computer Vision with OpenCV

A collection of classic computer vision techniques implemented with OpenCV — detection, tracking, calibration, and image transforms.

## Scripts

| Script | Technique |
|---|---|
| `facedetection.py` | Real-time face detection from webcam (Haar cascade) |
| `cardetection.py` | Car detection in video (Haar cascade) |
| `edgedetection.py` | Edge detection — Sobel gradient magnitude vs. Canny |
| `featuredetectionSIFT.py` | SIFT keypoint matching between two images |
| `KLTfeaturetracker.py` | Kanade-Lucas-Tomasi optical-flow feature tracking across video frames |
| `cameracalibration.py` | Camera calibration from a checkerboard pattern (camera matrix, distortion coefficients, reprojection error) |
| `histogram.py` | Grayscale intensity histograms + histogram equalization |
| `negative_image.py` | Photographic negative (intensity inversion) |
| `log_transform.py` | Log intensity transform for dynamic-range compression |
| `video.py` | Minimal video playback utility |

## Setup

```bash
pip install -r requirements.txt
```

## Required assets (not included)

These scripts operate on images/video you provide — OpenCV examples typically expect specific input files in the working directory:

- `facedetection.py`, `cameracalibration.py` — a live camera (index 0)
- `cardetection.py` — `cars.xml` (a car Haar cascade; not bundled with OpenCV — a few are available from community cascade collections) and `video.avi`
- `edgedetection.py` — `input.jpg`
- `featuredetectionSIFT.py` — `book.jpg`, `table.jpg` (any two images with shared visual features work)
- `KLTfeaturetracker.py` — `input_video.mp4`
- `cameracalibration.py` — a printed 7x6-corner checkerboard, plus `test.jpg` to undistort
- `histogram.py`, `negative_image.py`, `log_transform.py` — `input_image.jpg`
- `video.py` — `video.mp4`

Face detection uses OpenCV's bundled Haar cascade (`cv2.data.haarcascades`), so no external file is needed for that one.

## Tech stack

Python, OpenCV (`opencv-python` + `opencv-contrib-python` for SIFT), NumPy, Matplotlib
