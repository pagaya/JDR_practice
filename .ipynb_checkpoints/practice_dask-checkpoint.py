# %pip install dask --upgrade
import pandas as pd
import dask.dataframe as dd


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
# %pip install graphviz
# import os
# os.environ["PATH"] += os.pathsep + '/Users/johnros/workspace/practicing/venv/lib/python3.8/site-packages/graphviz'
# ddf.groupby(['a', 'b']).c.sum().visualize()



### Tutorial #2:
# %pip install "dask[distributed]" --upgrade
from dask.distributed import Client

client = Client(n_workers=1, threads_per_worker=4, processes=False, memory_limit='2GB')
client
