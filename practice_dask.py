### VScode does not like Dask!!!

# %pip install dask --upgrade
import pandas as pd
import dask.dataframe as dd


### Dask DataFrames
import dask
import dask.dataframe as dd
df = dask.datasets.timeseries()

import pandas as pd
df.head(3)

df2 = df[df.y > 0]
df3 = df2.groupby('name').x.std()
df3.compute()

df = df.persist()
df.compute()



### Dask bags
import dask
import json
import os

os.makedirs('data', exist_ok=True)              # Create data/ directory
b = dask.datasets.make_people()  
type(b)               # Make records of people
b.map(json.dumps).to_textfiles('data/*.json')   # Encode as JSON, write to disk

!head -n 2 data/0.json

import dask.bag as db
import json

b = db.read_text('data/*.json').map(json.loads)
b






### Manual versus Dask

df = pd.DataFrame(dict(a=[1, 1, 2, 3, 3, 1, 1, 2, 3, 3, 99, 10, 1],
                        b=[1, 3, 10, 3, 2, 1, 3, 10, 3, 3, 12, 0, 9],
                        c=[2, 4, 5, 2, 3, 5, 2, 3, 9, 2, 44, 33, 2]))
df

# Manual split-apply-combine
df_1 = df[:5]
df_2 = df[5:10]
df_3 = df[-3:]

sr1 = df_1.groupby(['a', 'b']).c.sum()
sr2 = df_2.groupby(['a', 'b']).c.sum()
sr3 = df_3.groupby(['a', 'b']).c.sum()

sr_concat = pd.concat([sr1, sr2, sr3])
sr_concat
total = sr_concat.groupby(level=[0, 1]).sum()


ddf = dd.from_pandas(df, npartitions=3)



### Working with clients
# %pip install "dask[distributed]" --upgrade
import dask
from dask.distributed import Client

client = Client(n_workers=1, threads_per_worker=4, processes=False, memory_limit='2GB')
client


df = dask.datasets.timeseries()
df
df = df.persist()
