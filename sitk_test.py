import numpy as np
import SimpleITK as itk
from utils import *
import cv2 as cv

if __name__ == '__main__':
    itk_img = itk.ReadImage('Dataset_Group/04/images/BRATS_259_Tumor.nii.gz')
    img = itk.GetArrayFromImage(itk_img)
    #print(np.histogram(img))
    img = img.transpose(1, 2, 0)
    width, height, queue = img.shape
    #print(width, height, queue)
    # print(img[84][148][83])
    # for i in range(width):
    #     for j in range(height):
    #         for k in range(queue):
    #             if img[i][j][k]>1000:
    #                 print(i,j,k,img[i][j][k])
    #cv.imwrite('1.jpg', img[:, :, 100])
    show2D(img)
