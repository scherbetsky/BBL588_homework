#finding the histogram
import matplotlib.pyplot as plt
import cv2
import os
os.chdir('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\')
hist_img = cv2.imread("I.png",0) #selecting the grayscale image
plt.hist(hist_img.ravel(),256,[0,256]) #ploting the histogram of the image from 0 to 256
plt.show()
h = cv2.calcHist([hist_img], [0], None,[256],[0,256]) # h variable as the array of histogram values.

#finding threshold T
T, tresh = cv2.threshold(hist_img, 127,255,cv2.THRESH_BINARY)
print("Threshold value is = ",T)
plt.imshow(tresh, 'gray')
plt.show() #presenting the binary image B
