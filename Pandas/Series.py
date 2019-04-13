import pandas as pd 

a=pd.Series([1,2,3,4,5])
print(a)

print(a[3])

dt=pd.date_range(start='01-01-2019',end='13-04-2019')
print(dt)