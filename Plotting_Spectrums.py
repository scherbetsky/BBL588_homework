import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import os
os.chdir("C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\")

#getting the fourier transform of the images
img_1 = cv2.imread("I_1.png", 0)
f_1 = np.fft.fft2(img_1)
fshift_1 = np.fft.fftshift(f_1) #in order to shift the zero freq component into center
magnitude_spectrum_1 = 20*np.log(np.abs(fshift_1)) #magnitude formula

plt.subplot(121),plt.imshow(img_1, cmap = 'gray')
plt.title('I_1'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum_1, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
