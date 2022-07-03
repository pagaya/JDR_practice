%pip install polars

import polars as pl
df= pl.DataFrame({'City':['A','B','C','D','E','F','G','H'],
                  'Temperature':[30.5,32,25,38,40,29.6,21.3,24.9],
                  'Rain':[103,125,90,75,130,200,155,127]
                 })

type(df)

df.dtypes
df.columns
df.head()