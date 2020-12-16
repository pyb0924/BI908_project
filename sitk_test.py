import numpy as np
import SimpleITK as itk
from utils import *
import cv2 as cv

if __name__ == '__main__':
    itk_img = itk.ReadImage('Dataset_Group/01/images/BRATS_027_Tumor.nii.gz')
    img = itk.GetArrayFromImage(itk_img)
    print(np.histogram(img))
    img = img.transpose(1, 2, 0)
    width, height, queue = img.shape
    print(width, height, queue)
    #cv.imwrite('1.jpg', img[:, :, 100])
    show2D(img, queue)
