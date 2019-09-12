import numpy as np
import sys
import cv2

image = cv2.imread("D:\\OpenCV\\1.jpg")

new_image = np.zeros(image.shape, image.dtype)

brightness_value = int(input("Enter brightness value [0-100]: "))
contrast_value = float(input("Enter contrast value [1.0-3.0]: "))

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(contrast_value*image[y,x,c] + brightness_value, 0, 255)

cv2.imshow('image', image)

cv2.imshow('edited image', new_image)
print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()