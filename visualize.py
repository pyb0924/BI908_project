from utils import read_img
from pathlib import Path
from config import data_path
import matplotlib.pyplot as plt


output_path= Path('output')
methods=[
    'multi_threshold_otsu','otsu_with_opening_closing',
    'traditional_region_growing','new_region_growing','new_region_growing_with_closing'
]
samples={
    'BRATS_008_Output.nii.gz':60,
    'BRATS_033_Output.nii.gz':70,
    'BRATS_259_Output.nii.gz':110
}


if __name__ == "__main__":
    fig,axes=plt.subplots(3,6)
    plt.subplots_adjust(wspace=0, hspace=0)

    for i,(sample,q_to_disp) in enumerate(samples.items()):
        for j,method in enumerate(methods):
            img=read_img(str(output_path /method / sample))
            ax=axes[i,j]
            ax.imshow(img[:,:,q_to_disp],cmap='gray')
            ax.axis('off')
            
        label_name=sample.replace('Output','Seg')
        img=read_img(str(data_path/'labels'/label_name))
        ax=axes[i,5]
        ax.imshow(img[:,:,q_to_disp],cmap='gray')
        ax.axis('off')

    plt.tight_layout()
    plt.savefig('result.png',dpi=600)
    plt.show()
    
            

