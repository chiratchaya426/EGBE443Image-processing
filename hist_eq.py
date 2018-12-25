import cv2
import numpy as np
from matplotlib import pyplot as plt 

img=cv2.imread('cat-jpg.jpg',0)
plt.hist(img_jp.ravel(),256,[0,256]);
plt.show()
plt.hist(img_jp.ravel(),256,[0,256], cumulative = True); 
plt.show()
img_eq = cv2.equalizeHist(img)
equ = np.hstack((img,img_eq)) #stacking images side-by-side
cv2.imwrite('equ.png',equ)
plt.hist(img_eq.ravel(),256,[0,256]);
plt.show()
plt.hist(img_eq.ravel(),256,[0,256], cumulative = True); 
plt.show()