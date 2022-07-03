import numpy as np
import pandas as pd

a={}
a[1] = np.empty(shape=(100,1))
a[2] = np.empty(shape=(100,1))

pd.DataFrame.from_dict(a, orient='index')

pd.DataFrame()