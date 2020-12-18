from sklearn.metrics import confusion_matrix
import numpy as np
output = np.array([0, 1, 0, 1, 0, 0, 1])
label = [0, 0, 1, 0, 0, 0, 0]

if __name__ == '__main__':
    print(np.sum(output>0))
