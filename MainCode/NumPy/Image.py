import cv2
import numpy as np
d = cv2.data.haarcascades

img = cv2.imread('image.png',0)
#print(img)
 # 0: grayscale and 1: BGR
# cv2.imwrite("ashish.png",img) #For creating an image
#----------------------------------Slicing------------------------------------------------------------------------------
k=(img[0:2])
#print(k.shape)
#print(img[0:2,2:4])

#--------------------------------------------Iterating------------------------------------------------------------------
#for i in img.T:
    #T is transpose(iterate through columns)
    #print(i)
#for j in img.flat: #Value by value
    #print(j)

#----------------------------------Concatinating------------------------------------------------------------------------

imh = np.hstack((img,img)) # Horizontal stacking
imv = np.vstack((img,img)) # vertical stacking for concatinating two arrays
#print(ims)

#-------------------------------------Splitting-------------------------------------------------------------------------

imhsp = np.hsplit(img,3)
imvsp = np.vsplit(img,6)
print(imvsp)