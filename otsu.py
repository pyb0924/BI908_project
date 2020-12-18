import numpy as np
from utils import *


def otsu2Threshold(img, t):
    src = img * 255 / np.max(img)
    threshold1 = 0
    threshold2 = 0
    theta = 1
    weight, height, queue = np.shape(src)
    hest = np.zeros([256], dtype=np.int32)
    for row in tqdm(range(weight)):
        for col in range(height):
            for shi in range(queue):
                pv = src[row, col, shi]
                hest[int(pv)] += 1
    tempg = -1
    N_blackground = 0
    N_object = 0
    N_all = weight * height * queue
    for k in range(t):
        N_all -= hest[k]

    for i in tqdm(range(t, 256)):
        N_object += hest[i]
        for k in range(i+1, 256, 1):
            N_blackground += hest[k]
        for j in range(i+1, 256, 1):
            gSum_object = 0
            gSum_middle = 0
            gSum_blackground = 0

            N_middle = N_all - N_object - N_blackground
            w0 = N_object / N_all
            w2 = N_blackground / N_all
            w1 = 1 - w0 - w2
            for k in range(i):
                gSum_object += k * hest[k]
            u0 = gSum_object / N_object
            for k in range(i + 1, j, 1):
                gSum_middle += k * hest[k]
            u1 = gSum_middle / (N_middle + theta)

            for k in range(j + 1, 256, 1):
                gSum_blackground += k * hest[k]
            u2 = gSum_blackground / (N_blackground + theta)

            u = w0 * u0 + w1 * u1 + w2 * u2
            g = w0 * (u - u0) * (u - u0) + w1 * (u - u1) * (u - u1) + w2 * (u - u2) * (u - u2)
            if tempg < g:
                tempg = g
                threshold1 = i
                threshold2 = j
            N_blackground -= hest[j]

    weight, height, queue = np.shape(src)
    im = np.zeros([weight, height, queue])
    for row in tqdm(range(weight)):
        for col in range(height):
            for shi in range(queue):
                if src[row, col, shi] > threshold2:
                    im[row, col, shi] = 1
                elif src[row, col, shi] <= threshold1:
                    im[row, col, shi] = 0
                else:
                    im[row, col, shi] = 0
    return im, threshold1, threshold2
