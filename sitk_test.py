import numpy as np
import SimpleITK as itk
from utils import *
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img=read_img('Dataset_Group/04/images/BRATS_033_Tumor.nii.gz')
    label=read_img('Dataset_Group/04/labels/BRATS_033_Seg.nii.gz')
    print(np.sum(label))
    print(np.sum(img>850))
