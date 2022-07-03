a= [1,2,3]
b= [4,5]
(a,b)
[print(x) for y in  (a,b) for x in 



import pandas as pd
df = pd.DataFrame([[1, 2], [1, 4], [5, 6]], columns=['a', 'b']).set_index('a')

pd.concat([df, df.groupby(level=0).shift()], axis=1, ignore_index=True).dropna()


pd.Series([1 for x in range(100)]).rolling(4, min_periods=1, center=True).sum()