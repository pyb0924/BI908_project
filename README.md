# BI908 多种方法实现的脑肿瘤分割

BI908生物医学图像处理（1）大作业。对给定的脑肿瘤图像进行分割。采用Otsu多阈值处理，区域增长方法和形态学处理算法综合实现。
## Overview

- main.py 主函数
- iotest.py/sitk_test.py 调试文件（不要运行）
- prepare.py 数据切片成二维图（可供deep learning使用）
- otsu.py 实现三维多阈值Otsu算法
- region_growing.py 实现region_growing算法
- validation.py 计算评价指标
- visualize.py 显示可视化结果
- config.py 存放算法运行中所需的各常数
- utils.py 实现其他所需的函数（图像I/O，可视化，形态学操作）

## Run
- run.bat 修改参数--method对应的值即可使用不同方法。
- 若要修改运行时使用的参数常量，进入config.py修改即可。
- 在每次运行之前建议清空result.json为'[]'，以区分多次结果。

## Dependencies
- 见requirements.txt
