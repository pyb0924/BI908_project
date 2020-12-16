import numpy as np
from pathlib import Path
from tqdm import tqdm
import SimpleITK as itk
import cv2 as cv
import matplotlib.pyplot as plt

dataset_path = Path('Dataset_Group')
train_path = Path('train_data')

test_path = Path('test_data')

if __name__ == '__main__':
    for dataset_index in tqdm(range(1, 10)):
        data_folder = '0' + str(dataset_index)
        (train_path / data_folder / 'images').mkdir(exist_ok=True, parents=True)
        (train_path / data_folder / 'labels').mkdir(exist_ok=True, parents=True)
        image_list=list((dataset_path / data_folder / 'images').glob(('*.gz')))
        for file_name in image_list:
            itk_img = itk.ReadImage(str(file_name))
            img = itk.GetArrayFromImage(itk_img)
            img = img.transpose(1, 2, 0)
            width, height, queue = img.shape
            for layer in range(queue):
                img_to_write=img[:,:,layer]/np.max(img)*255
                img_to_write = cv.cvtColor(img_to_write, cv.COLOR_GRAY2BGR)
                img_to_write=cv.resize(img_to_write,(256, 256), cv.INTER_AREA)
                cv.imwrite(str(train_path / data_folder / 'images' / (file_name.stem + str(layer) + '.jpg')),
                           img_to_write)

        label_list=list((dataset_path / data_folder / 'labels').glob(('*.gz')))
        for file_name in label_list:
            itk_img = itk.ReadImage(str(file_name))
            img = itk.GetArrayFromImage(itk_img)
            img = img.transpose(1, 2, 0)
            width, height, queue = img.shape
            #print(np.histogram(img),queue)
            for layer1 in range(queue):
                img_to_write=img[:,:,layer1]*255
                img_to_write = cv.cvtColor(img_to_write, cv.COLOR_GRAY2BGR)
                img_to_write=img_to_write.resize((256,256),cv.INTER_AREA)
                cv.imwrite(str(train_path / data_folder / 'labels' / (file_name.stem + str(layer1) + '.jpg')),
                           img_to_write)

    print('done!')

