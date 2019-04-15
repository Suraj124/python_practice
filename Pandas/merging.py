import pandas as pd 

DF1=pd.DataFrame([['a',1],['b',2]],columns=['col1','number'])
DF2=pd.DataFrame([['c',3,'lion'],['d',4,'tiger']],columns=['letter','number','animal'])

# print(DF1)
# print(DF2)

#concat()-->It will concatinate 2 DataFrames
#concatination in rows

# print(pd.concat([DF1,DF2],axis=0))
# print(pd.concat([DF1,DF2],axis=0 , ignore_index=True))

#concatination in columns

print(pd.concat([DF1,DF2],axis=1))
