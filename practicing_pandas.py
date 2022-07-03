from cgi import test
from cmath import log
import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
df

## Query
df.query('4 <= c <=7')

## Grouby
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
groups = df.groupby('Animal')

for name,group in groups:
    group['test']=0


new={}
for name,group in groups:
    new[name] = group['Max Speed']
    print(new[name])
    new[name]=0

new

for name,group in groups:
    print(group)


#### Performance


