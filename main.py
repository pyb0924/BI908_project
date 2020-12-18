from utils import *
from config import *
from validation import get_all_validation
from region_growing import region_growing
from otsu import otsu2Threshold
import argparse
import numpy as np
import time


def run_otsu(image_names):
    for image_name in image_names:
        print('begin processing: ' + str(image_name))
        img = read_img(str(image_name))
        label_name = str(image_name).replace('images', 'labels').replace('Tumor', 'Seg')
        label = read_img(label_name)
        output_name = (str(image_name).split('\\')[3]).replace('Tumor', 'Output')

        # multi-threshold Otsu
        time_start=time.time()
        output_path = root_path / 'output' / 'multi_threshold_otsu'
        output_path.mkdir(exist_ok=True, parents=True)
        print('Reading finished, begin Otsu (multi-threshold)')
        img_otsu, threshold1, threshold2 = otsu2Threshold(img, OTSU_BG)
        print('Otsu threshold 1: ' + str(threshold1) + '   ' + 'Otsu threshold 2: ' + str(threshold2))
        write_img(img_otsu, str(output_path / output_name))
        time_end1=time.time()

        valid_results = get_all_validation(img_otsu, label, str(image_name), 'multi-threshold Otsu')
        valid_results['time_cost']=time_end1-time_start
        print(valid_results)
        write_result(valid_results, result_file_name)
        print('\n')

        # Otsu with opening and closing (This part may be executed very slowly)
        output_path2 = root_path / 'output' / 'otsu_with_opening_closing'
        output_path2.mkdir(exist_ok=True, parents=True)
        print('begin closing operation')
        img_otsu2 = closing(img_otsu, 3)
        print('begin opening operation')
        img_otsu2 = opening(img_otsu2, 3)
        write_img(img_otsu2, str(output_path2 / output_name))
        time_end2=time.time()

        valid_results = get_all_validation(img_otsu2, label, str(image_name), 'Otsu_with_opening_closing')
        valid_results['time_cost']=time_end2-time_start
        print(valid_results)
        write_result(valid_results, result_file_name)
        print('\n')


def run_rg(image_names):
    for image_name in image_names:
        img = read_img(str(image_name))
        label_name = str(image_name).replace('images', 'labels').replace('Tumor', 'Seg')
        label = read_img(label_name)
        output_name = (str(image_name).split('\\')[3]).replace('Tumor', 'Output')

        # traditional region_growing
        time_start=time.time()
        output_path = root_path / 'output' / 'traditional_region_growing'
        output_path.mkdir(exist_ok=True, parents=True)
        print('Reading finished, begin region growing')
        # print(np.sum(label))
        img_rg = region_growing(img, GROWING_NEIGHBOR, 2, seed[output_name], False, np.sum(img > 850))
        write_img(img_rg, str(output_path / output_name))
        time_end1=time.time()

        valid_results = get_all_validation(img_rg, label, str(image_name), 'traditional_region_growing')
        valid_results['time_cost']=time_end1-time_start
        print(valid_results)
        write_result(valid_results, result_file_name)
        print('\n')

        # new region_growing (This part may be executed very slowly)
        time_start=time.time()
        output_path2 = root_path / 'output' / 'new_region_growing'
        output_path2.mkdir(exist_ok=True, parents=True)
        print('begin region growing')
        img_rg2 = region_growing(img, GROWING_NEIGHBOR, 2, seed[output_name], True, np.sum(img > 850))
        write_img(img_rg2, str(output_path2 / output_name))
        time_end1=time.time()

        valid_results = get_all_validation(img_rg2, label, str(image_name), 'new_region_growing')
        valid_results['time_cost']=time_end1-time_start
        print(valid_results)
        write_result(valid_results, result_file_name)
        print('\n')

        # new region growing with closing (This part may be executed very slowly)
        output_path3 = root_path / 'output' / 'new_region_growing_with_closing'
        output_path3.mkdir(exist_ok=True, parents=True)
        print('begin closing operation')
        img_rg3 = closing(img_rg2, 3)
        write_img(img_rg3, str(output_path3 / output_name))
        time_end2=time.time()

        valid_results = get_all_validation(img_rg3, label, str(image_name), 'new_region_growing_with_closing')
        valid_results['time_cost']=time_end2-time_start
        print(valid_results)
        write_result(valid_results, result_file_name)
        print('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('--method', type=str, default='all', choices=['otsu', 'rg', 'all'])
    args = parser.parse_args()

    image_names = (data_path / 'images').glob('*')
    if args.method == 'otsu':
        run_otsu(image_names)
    elif args.method == 'rg':
        run_rg(image_names)
    elif args.method == 'all':
        run_otsu(image_names)
        image_names = (data_path / 'images').glob('*')
        run_rg(image_names)

    print('done!')
