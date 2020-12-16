import matplotlib.pyplot as plt
import SimpleITK as itk
from tqdm import tqdm
from pathlib import Path
from nibabel.viewers import OrthoSlicer3D
import json

'''
    ----------Header----------
    constant:
        root_path
        result_file_name
        OTSU_BG
        GROWING_NEIGHBOR
        RG_THRESHOLD
        seed(dict)
        
        
    image file operation:
        read_img(img_path:str)
        write_img(img: 3d-array ,img_path:str)
        show2D(img: 3d-array, queue:int) # queue: depth of figure
        show3D(img: 3d-array)
        write_result(data:dict)
        
    basic operation:
        dilate(img: 3d-array, t:int) # t: structuring_element_size = 2*t + 1
        erode(img: 3d-array, t:int) 
        closing(img: 3d-array, t:int) 
        opening(img: 3d-array, t:int)
        
'''
root_path = Path('')
data_path = Path('Dataset_Group/04')
result_file_name = 'result.json'
OTSU_BG = 10
GROWING_NEIGHBOR = 2
RG_THRESHOLD = 4
seed = {'BRATS_008_Output.nii.gz':[84,148,83]}
result_keys = ['sample_name', 'method', 'sensitivity', 'specificity','precision', 'accuracy', 'iou', 'dice']


def read_img(img_path):
    itk_img = itk.ReadImage(img_path)
    im = itk.GetArrayFromImage(itk_img)
    im = im.transpose(1, 2, 0)
    return im


def write_img(img, img_path):
    img = img.transpose(2, 0, 1)
    img_out = itk.GetImageFromArray(img)
    itk.WriteImage(img_out, img_path)
    return


def show2D(img):
    num = 1
    queue = img.shape[2]
    for i in range(0, queue, 10):
        img_arr = img[:, :, i]
        plt.subplot(5, 4, num)
        plt.imshow(img_arr, cmap='gray')
        num += 1
    plt.show()


def show3D(img):
    OrthoSlicer3D(img).show()


def write_result(result, file_name):
    with open(file_name, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        f.seek(0, 0)
        data.append(result)
        json.dump(data, f, indent=4, ensure_ascii=False)
    return

def dilate(im,t):
    newimg=im+0
    n,m,l=im.shape
    print('dilate')
    for i in tqdm(range(n)):
        for j in range(m):
            for k in range(l):
                if (im[i][j][k]!=0):
                    for ii in range(-t,t+1):
                        for jj in range(-t,t+1):
                            for kk in range(-t,t+1):
                                if (i+ii>=0)and(i+ii<=n)and(j+jj>=0)and(j+jj<=m)and(k+kk>=0)and(k+kk<=l):
                                    newimg[i+ii][j+jj][k+kk]=1
    print()
    return newimg

def erode(im,t):
    newimg=im+0
    n,m,l=im.shape
    print('erode')
    for i in tqdm(range(n)):
        for j in range(m):
            for k in range(l):
                if (im[i][j][k]!=0):
                    flag=0
                    for ii in range(-t,t+1):
                        for jj in range(-t,t+1):
                            for kk in range(-t,t+1):
                                if (i+ii>=0)and(i+ii<=n)and(j+jj>=0)and(j+jj<=m)and(k+kk>=0)and(k+kk<=l):
                                    if (im[i+ii][j+jj][k+kk]==0):
                                        flag=1
                    if flag:
                        newimg[i][j][k]=0
    print()
    return newimg

def closing(im, t):
    tmp = dilate(im, t)
    return erode(tmp, t)


def opening(im, t):
    tmp = erode(im, t)
    return dilate(tmp, t)
