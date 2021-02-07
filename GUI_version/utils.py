import matplotlib.pyplot as plt
import SimpleITK as itk
from nibabel.viewers import OrthoSlicer3D
import json
import numpy as np
from scipy.signal import convolve2d

'''
    ----------Header----------
    
    image file operation:
        read_img(img_path:str)
        write_img(img: 3d-array ,img_path:str)
        show2D(img: 3d-array, queue:int) # queue: depth of figure
        show3D(img: 3d-array)
        write_result(data:dict)
        
    basic operation:
        dilate(img: 3d-array, t:int) # t: structuring_element_size = 2*t + 1
        erode(img: 3d-array, t:int) 
        convolve3d(img: 3d-array, kernal: 3d-array)
        closing(img: 3d-array, t:int) 
        opening(img: 3d-array, t:int)
        
'''


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


def convolve3d(img, kernel):
    n, m, l = img.shape
    kn, km, kl = kernel.shape
    img_convolve3d = np.zeros([n, m, l])
    kn = int((kn - 1) / 2)
    # print(kn)
    for i in range(-kn, kn + 1):
        img_convolve2d = np.zeros([n, m, l])
        for j in range(n):
            if (i + j >= 0) and (i + j < n):
                img_convolve2d[i + j] = convolve2d(img[j], kernel[i + kn], boundary='symm', mode='same')
        img_convolve3d += img_convolve2d
    return img_convolve3d


def dilate(im, t):
    print('begin dilate')
    kernel = np.ones([2 * t + 1, 2 * t + 1, 2 * t + 1])
    newimg = convolve3d(im, kernel)
    newimg[newimg > 0] = 1
    return newimg


def erode(im, t):
    print('begin erode')
    kernel = np.ones([2 * t + 1, 2 * t + 1, 2 * t + 1])
    newimg = convolve3d(im, kernel)
    k = int(np.power(2 * t + 1, 3))
    newimg[newimg < k] = 0
    newimg[newimg == k] = 1
    return newimg


def closing(im, t):
    tmp = dilate(im, t)
    return erode(tmp, t)


def opening(im, t):
    tmp = erode(im, t)
    return dilate(tmp, t)
