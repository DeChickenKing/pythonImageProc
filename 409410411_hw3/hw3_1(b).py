import numpy as np
import cv2
import math

matrix=np.array ([[10,20,30],[40,50,60],[70,80,90]])
print (matrix.shape)

def dlin(input_signal, zoom_multiples) :
    ipr,ipc = input_signal.shapes
    outr = 5
    outc = 5
    output_signal = np.zeroes (outr,outc)
    for i in range (outr):
        for j in range (outc):
            temp_x = i / outr * ipr
            temp_y = j / outc * ipc
            x1 = int(temp_x)
            y1 = int(temp_y)
            x2 = x1; y2 = y1 + 1
            x3 = x1 + 1; y3 = y1 + 1
            x4 = x1 + 1; y4 = y1 + 1
            t = temp_x - x1; u = temp_y - y1
            if x4 >= ipr:
                x4 = ipr - 1
                x2 = x4
                x1 = x4 - 1
                x3 = x4 - 1
            if y4 >= ipr:
                x4 = ipr - 1
                x2 = x4
                x1 = x4 - 1
                x3 = x4 - 1
            output_signal[i,j] = {
                (i-1)*(i-u)*input_signal[x1,y1]
                +(1-t)*input_signal[x2,y2] + t*(1-u)*input_signal[x3,y3]
                +t*u*input_signal[x4,y4]
            }
    return output_signal