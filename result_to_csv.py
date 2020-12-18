import pandas as pd
import numpy as np
import json


if __name__ == '__main__':
    with open('result.json','r')as f:
        data=json.load(f)
    df=pd.DataFrame(data)
    df.index=df.set_index(['sample_name','method']).index
    df.drop(['sample_name','method','specificity','accuracy'],axis=1,inplace=True)
    df.to_csv('result.csv')
    print('done!')