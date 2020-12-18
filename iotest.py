from utils import *

# Only test I/O, don't run it!
if __name__ == '__main__':
    test_image_path = data_path / 'images' / 'BRATS_008_Tumor.nii.gz'
    img = read_img(str(test_image_path))
    print('read finished!')
    show2D(img)
    show3D(img)
    #write_img(img,'iotest.nii.gz')

    #new_img=read_img('iotest.nii.gz')
    #print('new image read finished!')
    #show2D(new_img)
    #show3D(new_img)

