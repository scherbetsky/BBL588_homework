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


kernel_25 = np.ones((5,5),np.float32)/25 #5x5 kernel with the value 1/25
dst_1_25 = cv2.filter2D(img_1,-1,kernel_25) #filter2D command convolves the kernel with image
dst_5_25 = cv2.filter2D(img_5,-1,kernel_25)
dst_10_25 = cv2.filter2D(img_10,-1,kernel_25)
dst_20_25 = cv2.filter2D(img_20,-1,kernel_25)


kernel_9 = np.ones((3,3),np.float32)/9 #3x3 kernel with the value 1/9
dst_1_9 = cv2.filter2D(img_1,-1,kernel_9) #filter2D command convolves the kernel with image
dst_5_9 = cv2.filter2D(img_5,-1,kernel_9)
dst_10_9 = cv2.filter2D(img_10,-1,kernel_9)
dst_20_9 = cv2.filter2D(img_20,-1,kernel_9)

# Drawing kernel_25 filtered images

plt.subplot(121),plt.imshow(img_1),plt.title('I_1')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_1_25),plt.title('LPF 1/25')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_5),plt.title('I_5')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_5_25),plt.title('LPF 1/25')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_10),plt.title('I_10')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_10_25),plt.title('LPF 1/25')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_20),plt.title('I_20')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_20_25),plt.title('LPF 1/25')
plt.xticks([]), plt.yticks([])
plt.show()

# Drawing kernel_9 filtered images

plt.subplot(121),plt.imshow(img_1),plt.title('I_1')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_1_9),plt.title('LPF 1/9')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_5),plt.title('I_5')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_5_9),plt.title('LPF 1/9')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_10),plt.title('I_10')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_10_9),plt.title('LPF 1/9')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(img_20),plt.title('I_20')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_20_9),plt.title('LPF 1/9')
plt.xticks([]), plt.yticks([])
plt.show()
