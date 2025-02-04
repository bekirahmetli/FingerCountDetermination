# FingerCountDetermination
## Libraries Used

- **OpenCV**: A library for image processing and computer vision.
- **NumPy**: A library for numerical calculations and array operations.

## Working Logic of the Project

1. **Image Capture**: Image is captured from the camera in real time.
2. **ROI Determination**: A specific region (ROI) of the image is selected and operations are performed on this region.
3. **Grayscale and Histogram Equalization**: The ROI region is converted to grayscale and contrast is increased by histogram equalization.
4. **Noise Reduction**: Noise in the image is reduced with Gaussian Blur.
5. **Warping**: The image is converted to binary format and the fingerprint is made more distinct.
6. **Contour Finding**: Contours are found on the binary image and the largest contour is selected.
7. **Finger Number Detection**: The number of fingers is determined using convex curves and errors.
8. **Result Display**: The number of fingers detected and processed images are shown on the screen.

![image](https://github.com/bekirahmetli/FingerCountDetermination/blob/main/image.png)

## Screen Output

Frame: Original camera image

Gray ROI: Grayscale translated region

Threshold: Thresholded image

Finger Count: The number of fingers detected is printed on the screen.
