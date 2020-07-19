# from datatime import datetime
import random
# import numpy as np


def createDF_fromdir_csv(path):
    import pandas as pd
    import glob
    """
    This will create dataframe from a dir with all csv files in it
    input param: 
    """
    all_files = glob.glob(path + "/*.csv")
    li = []
    for file in all_files:
        df = pd.read_csv(file, header=0, index_col=None)
        li.append(df)

    all_data = pd.concat(li, axis=0, ignore_index=True)
    return all_data





T = 100

def do_product_withNP(a,  b):
    dot = 0
    # print(a,b)
    # b
    for i , j in zip(a,b):
        # print(i, j)
        dot += i * j
        # print(dot)
    return dot

a = [random.randrange(1,10,1,int)]
b = [random.randrange(1,10,1,int)]

for i in range(10):
    print(do_product_withNP(a,b))

random.randint()

# print(a)