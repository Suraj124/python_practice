import pandas as pd
import numpy as np

temp=np.random.randint(10,50,20)
name=np.random.choice(['Suraj','Tarun','Piyush','Anjesh','Subran',],20)
num=np.random.choice([23,34,54,67,19],20)

DF=pd.DataFrame({'Temp':temp,'Name':name,'Num':num})
print(DF.head())

#iloc()--> is used by indexes
print(DF.iloc[[2,4]])
print('\n')
print(DF.iloc[1:5,:2])  #1 to 4 row and 0 to 1 column

DF.set_index('Name',inplace=True)
print(DF)
print('\n')
#loc()--> is used by given index of user
print(DF.loc['Suraj'])
print(DF.loc[['Suraj','Subran']])
print('\n')
print(DF.loc[['Suraj','Subran'], 'Temp':'Num']) # show values of Suraj and subran.From column Name to Subran

#conditions
print('\n')
print(DF.loc[DF.Num>40])
print('\n')
DF.loc[(DF.Num>30) | (DF.Num==30) , :]
