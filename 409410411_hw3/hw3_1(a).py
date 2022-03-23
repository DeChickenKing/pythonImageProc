from numpy.matrixlib.defmatrix import matrix
import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

matrix=np.array ([[10,20,30],[40,50,60],[70,80,90]])
print (matrix.shape)

def NN_interpolation(img):
    srcH, srcW = img.shape
    dstH, srcW = 5,5
    retIMG = np.zeros([5,5],dtype = 'uint8')
    for i in range (5) :
        for j in range (5) :
            srcX = int (round (i) * (3/5))
            srcY = int (round (j) * (3/5))
            if srcX >= srcW:
                srcX = srcW -1
            if srcY >= srcH:
                srcY = srcH -1
            retIMG[i,j] = img[srcX,srcY]
    return retIMG

newIMG = NN_interpolation(matrix)
print ( newIMG.shape)
print ( newIMG )