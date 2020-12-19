from config import data_path
from utils import *

# Only test I/O, don't run it!
if __name__ == '__main__':
    test_image_path = data_path / 'labels' / 'BRATS_259_Seg.nii.gz'
    img = read_img(str(test_image_path))
    print('read finished!')
    show2D(img)

    result_path= 'output/new_region_growing/BRATS_259_Output.nii.gz'
    img = read_img(str(result_path))
    print('read finished!')
    show2D(img)
    # show3D(img)
    # write_img(img,'iotest.nii.gz')
    # new_img=read_img('iotest.nii.gz')
    # print('new image read finished!')
    # show2D(new_img)
    # show3D(new_img)

