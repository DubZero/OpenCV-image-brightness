import numpy as np
import sys
import cv2

# Edit brightness
def brightness(image, brightness_value):
	# Convert BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	height, width, channels = hsv.shape	
	for x in range(height):
		for y in range(width):
			if hsv[x,y,2] + brightness_value > 255:
				hsv[x,y,2] = 255
			elif hsv[x,y,2] + brightness_value < 0:
				hsv[x,y,2] = 0
			else:
				hsv[x,y,2] += brightness_value
				# Write new pixel channel value
	edit_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	return edit_img

# Edit contrast
def contrast(image, contrast_value):	
	height, width, channels = image.shape	
	for x in range(height):
		for y in range(width):
			for c in range(channels):
				if image[x,y,c] + contrast_value > 255:
					image[x,y,c] = 255
				elif image[x,y,c] + contrast_value < 0:
					image[x,y,c] = 0
				else:
					image[x,y,c] += contrast_value
	return image

image = cv2.imread("D:\\OpenCV\\1.jpg")

brightness_value = int(input("Enter brightness value: "))
contrast_value = int(input("Enter contrast value: "))
cv2.imshow('image', image)
if brightness_value != 0:
	image = brightness(image,brightness_value)
if contrast_value != 0:
	image = contrast(image,contrast_value)

cv2.imshow('edited image', image)
print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()