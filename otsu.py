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


# def deal(imgsource, labelsource, t1, t2):
#     img = read_img(imgsource)
#     n, m, l = img.shape
#     label = read_img(labelsource)
#     print('now otsu')
#     img_otsu, threshold1, threshold2 = otsu2Threshold(img, t1)
#     print('now closing-opperation')
#     closing_img = closing(img_otsu, t2)
#     newimg = opening(closing_img, t2)
#     print('the region-growing img shows as listed:')
#     show2D(img_otsu, l)
#     print('the closing-operation img shows as listed:')
#     show2D(newimg, l)
#     print('the label shows as listed:')
#     show2D(label, l)
#     im1 = label * newimg
#     im2 = label + newimg
#     I = np.sum(im1 != 0)
#     U = np.sum(im2 != 0)
#     print('IOU=', I / U)
#     print('the size of labels is ', np.sum(label != 0))
#     print('the size of newimg is ', np.sum(newimg != 0))
#     return newimg, I / U
#
#
# if __name__ == '__main__':
#     newimg, IoU = deal(imgsource, labelsource, t1, t2)

"""
img=read_img(imgsource)
n,m,l=img.shape
label=read_img(labelsource)
print('now otsu')
img_otsu,threshold1,threshold2 = Otsu2Threshold(img,t1)
print('now closing-opperation')
newimg=closing(img_otsu,t2)
newimg2=opening(newimg,t2)
print('the region-growing img shows as listed:')
show2D(img_otsu,l)
print('the closing-operation img shows as listed:')
show2D(newimg2,l)
print('the label shows as listed:')
show2D(label,l)
im1=label*newimg2
im2=label+newimg2
I=np.sum(im1!=0)
U=np.sum(im2!=0) 
print('IOU=',I/U)
print('the size of labels is ',np.sum(label!=0))
print('the size of newimg is ',np.sum(newimg2!=0))
"""
