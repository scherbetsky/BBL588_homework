import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import os
os.chdir("C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\")

# in order to filter images in frequency domain the fourier transforms of the images could be multiplied by masks with specific kernels
# if the non zero part of the mask is in the middle multiplication will give low frequency area therefore it is Low Pass Filter
# if the non zero part of the mask is in edges multiplication will give high frequency area therefore it is High Pass Filter
# then the image has to transform back to spatial domain
# multiplication in frequency domain means convolution in spatial doman and there is a tool for it in cv2 library


img_1 = cv2.imread('I_1.png')
img_5 = cv2.imread('I_5.png')
img_10 = cv2.imread('I_10.png')
img_20 = cv2.imread('I_20.png')

kernel_a = np.ones((3,3), np.float32) * (-1)
kernel_a[1][1] = 8

dst_1_a = cv2.filter2D(img_1,-1,kernel_a) #filter2D command convolves the kernel with image
dst_5_a = cv2.filter2D(img_5,-1,kernel_a)
dst_10_a = cv2.filter2D(img_10,-1,kernel_a)
dst_20_a = cv2.filter2D(img_20,-1,kernel_a)

kernel_b = np.ones((3,3), np.float32) * (17/100)
kernel_b[1][1] = (-1)*(333/100)
kernel_b[0][1] = 67/100
kernel_b[1][0] = 67/100
kernel_b[1][2] = 67/100
kernel_b[2][1] = 67/100

dst_1_b = cv2.filter2D(img_1,-1,kernel_b) #filter2D command convolves the kernel with image
dst_5_b = cv2.filter2D(img_5,-1,kernel_b)
dst_10_b = cv2.filter2D(img_10,-1,kernel_b)
dst_20_b = cv2.filter2D(img_20,-1,kernel_b)

# Drawing kernel_a filtered images

plt.subplot(121),plt.imshow(img_1),plt.title('I_1')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_1_a),plt.title('HPF a')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_5),plt.title('I_5')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_5_a),plt.title('HPF a')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_10),plt.title('I_10')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_10_a),plt.title('HPF a')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_20),plt.title('I_20')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_20_a),plt.title('HPF a')
plt.xticks([]), plt.yticks([])
plt.show()

# Drawing kernel_9 filtered images

plt.subplot(121),plt.imshow(img_1),plt.title('I_1')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_1_b),plt.title('HPF b')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_5),plt.title('I_5')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_5_b),plt.title('HPF b')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_10),plt.title('I_10')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_10_b),plt.title('HPF b')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_20),plt.title('I_20')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_20_b),plt.title('HPF b')
plt.xticks([]), plt.yticks([])
plt.show()
