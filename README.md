# HSV Color Range Detector using OpenCV

This project is a simple HSV color range detector implemented in Python using OpenCV. It allows users to specify lower and upper HSV color range values using trackbars and then applies a mask to the video feed from the camera to isolate pixels within the specified range.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation
You can install the required libraries using pip:
```
pip install opencv-python numpy
```

## Usage
1. Run the `color_range_detector.py` script.
2. Adjust the trackbars to set the lower and upper HSV color range values.
3. Press 'q' to exit the program.

## Trackbars
- `Lower-H`: Lower hue value (0-180)
- `Lower-S`: Lower saturation value (0-255)
- `Lower-V`: Lower value (brightness) value (0-255)
- `Upper-H`: Upper hue value (0-180)
- `Upper-S`: Upper saturation value (0-255)
- `Upper-V`: Upper value (brightness) value (0-255)

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

Feel free to customize it further to include additional details or sections as needed!
