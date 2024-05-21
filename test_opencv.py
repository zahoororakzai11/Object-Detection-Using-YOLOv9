import cv2
import numpy as np

# Create a blank image
image = np.zeros((500, 500, 3), np.uint8)

# Display the image in a window
cv2.imshow('Test Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()