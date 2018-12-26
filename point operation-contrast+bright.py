import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('cat-jpg.jpg',0)
#contrast
img_contrast = img*1.8
contrast = np.hstack((img,img_contrast)) #stacking images side-by-side
cv2.imwrite('contrast.png',contrast)

#brightness
img_bright = img+10
bright = np.hstack((img,img_bright)) #stacking images side-by-side
cv2.imwrite('bright.png',bright)
