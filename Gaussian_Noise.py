import cv2
import numpy as np
import PIL
from PIL import Image
import os
os.chdir('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\')
color_img = np.array(Image.open("C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\SunnyLake.bmp"))

mean = 0
deviation = [1, 5, 10, 20]
noisy_img = np.zeros(color_img.shape, np.float32)
                     
gaussian_1 = np.random.normal(mean, deviation[0], (300,400))

gaussian_5 = np.random.normal(mean, deviation[1], (300,400))

gaussian_10 = np.random.normal(mean, deviation[2], (300,400))

gaussian_20 = np.random.normal(mean, deviation[3], (300,400))
                       
for a in range(3):
        noisy_img[:,:,a] = color_img[:,:,a] + gaussian_1
Noisy_1 = Image.fromarray(noisy_img.astype('uint8'))
Noisy_1.save("Noisy_1.png")
Noisy_1.show()
for a in range(3):
        noisy_img[:,:,a] = color_img[:,:,a] + gaussian_5
Noisy_5 = Image.fromarray(noisy_img.astype('uint8'))
Noisy_5.save("Noisy_5.png")
Noisy_5.show()
for a in range(3):
        noisy_img[:,:,a] = color_img[:,:,a] + gaussian_10
Noisy_10 = Image.fromarray(noisy_img.astype('uint8'))
Noisy_10.save("Noisy_10.png")
Noisy_10.show()
for a in range(3):
        noisy_img[:,:,a] = color_img[:,:,a] + gaussian_20
Noisy_20 = Image.fromarray(noisy_img.astype('uint8'))
Noisy_20.save("Noisy_20.png")
Noisy_20.show()
