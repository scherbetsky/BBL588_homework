# The noise type on Figure_1 is salt and pepper noise
# This kind of noise is caused by too high and too low pixel values in the image
# By applying median filter this too high and too low pixel values can be replaced by overall median pixel value
# Median filter takes the median value and applies it to the extreme pixels

import cv2
import numpy as np
import os
os.chdir("C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\")

img = cv2.imread('Figure_1.png')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1) #side by side comparison

cv2.imshow('img', compare)
cv2.imwrite('Figure_1_denoised.png', compare)

