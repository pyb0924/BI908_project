from pathlib import Path

root_path = Path('')
data_path = Path('Dataset_Group/04')
result_file_name = 'result.json'
OTSU_BG = 10
GROWING_NEIGHBOR = 2
RG_THRESHOLD = 2
seed = {'BRATS_008_Output.nii.gz': [84, 148, 83], 'BRATS_033_Output.nii.gz': [85, 150, 75],
        'BRATS_259_Output.nii.gz': [120, 93, 116]}
result_keys = ['sample_name', 'method', 'sensitivity', 'specificity', 'precision', 'accuracy', 'iou', 'dice']



