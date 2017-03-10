import numpy as np
import cv2
image = cv2.imread("D:\\OpenCV\\1.jpg")
height, width, channels = image.shape	
alpha = input("Input alpha...")
beta = input("Input beta...")


for x in range(height):
	for y in range(width):
		for c in range(channels):
			# Write new pixel channel value
cv2.imshow('image', image)
print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()