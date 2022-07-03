import random
import pandas as pd
import numpy as np
from multiprocessing import  Pool




from math import sqrt
%pip install joblib
from joblib import Parallel, delayed
Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(10))




def my_fun():
    return(np.random.randn(10))
def parallel(fun):
    pool = Pool(2)
    result = pool.map(my_fun, range(3))
    pool.close()
    pool.join()
    return(result)

parallel(my_fun)



def add_features(df):
    df['question_text'] = df['question_text'].apply(lambda x:str(x))
    return df


def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores) # split along rows
    pool = Pool(n_cores) # create worker pool
    df = pd.concat(pool.map(func, df_split)) 
    pool.close()
    pool.join()
    return df


train = parallelize_dataframe(train_df, add_features)


