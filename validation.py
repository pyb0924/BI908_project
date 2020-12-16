from sklearn.metrics import confusion_matrix
from utils import result_keys
import numpy as np

'''
    ----------Header----------

    validation:
        cm(output: binary_array ,label: binary_array)
        iou(cm)
        dice(cm)
        
'''


def cal_cm(res, label):
    y_true = label.flatten()
    y_pred = res.flatten()
    return confusion_matrix(y_true, y_pred)


def get_iou(cm):
    return cm[1][1] / (cm[1][1] + cm[0][1] + cm[1][0])


def get_dice(cm):
    return 2 * cm[1][1] / (cm[0][1] + cm[1][0] + 2 * cm[1][1])


def get_sensitivity(cm):
    return cm[1][1] / (cm[1][1] + cm[0][1])


def get_specificity(cm):
    return cm[0][0] / (cm[0][0] + cm[1][0])

def get_precision(cm):
    return cm[1][1]/(cm[1][1]+cm[1][0])

def get_accuracy(cm):
    return (cm[0][0]+cm[1][1])/np.sum(cm)


def get_all_validation(res, label, image_name, method):
    cm = cal_cm(res, label)
    print(cm)
    sensitivity = get_sensitivity(cm)
    specificity = get_specificity(cm)
    precision=get_precision(cm)
    accuracy=get_accuracy(cm)
    iou = get_iou(cm)
    dice = get_dice(cm)
    
    valid_results = [sensitivity, specificity,precision, accuracy, iou, dice]
    result_values = [str(image_name), method] + valid_results
    result_dict = dict(zip(result_keys, result_values))
    return result_dict
