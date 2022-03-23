import numpy as np
import cv2
import math

matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(matrix.shape)
def double_linear(input_signal,zoom_multiples):
    input_row,input_col = input_signal.shape
    output_row = 5
    output_col = 5
    output_signal = np.zeros((output_row,output_col))
    for i in range(output_row):
        for j in range(output_col):
            temp_x = i / output_row * input_row
            temp_y = j / output_col * input_col
            x1 = int(temp_x)
            y1 = int(temp_y)
            x2 = x1;y2 = y1 + 1
            x3 = x1 + 1;y3 = y1
            x4 = x1 + 1;y4 = y1 + 1
            t = temp_x;u = temp_y - y1
        if x4 >= input_row:
            x4 = input_row -1
            x2 = x4
            x1 = x4 -1
            x3 = x4 -1
        if y4 >= input_col:
            y4 = input_col -1
            y3 = y4
            y1 = y4 -1
            y2 = y4 -1
        output_signal[i,j]=(1-t)*(1-u)*input_signal[x1,y1] + (1-
t)*u*input_signal[x2,y2] + t*(1-u)*input_signal[x3,y3]+t*u*input_signal[x4,y4]
    return output_signal
dstImg = double_linear(matrix,(5/3)).astype(np.uint8)
print(dstImg.shape)
print(dstImg)