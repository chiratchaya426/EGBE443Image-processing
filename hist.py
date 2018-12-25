import cv2
import numpy as np
from matplotlib import pyplot as plt 
  
img_jp = cv2.imread('cat-jpg.jpg',0)
plt.hist(img_jp.ravel(),256,[0,256]); 
plt.show()

img_pn = cv2.imread('cat-png.png',0)
plt.hist(img_pn.ravel(),256,[0,256]); 
plt.show()

img_bm = cv2.imread('cat-bmp.bmp',0)
plt.hist(img_bm.ravel(),256,[0,256]); 
plt.show()

img_ti = cv2.imread('cat-tiff.tiff',0)
plt.hist(img_ti.ravel(),256,[0,256]); 
plt.show()