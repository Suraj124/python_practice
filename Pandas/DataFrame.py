import pandas as pd
import numpy as np

temp=np.random.randint(10,50,20)
name=np.random.choice(['Suraj','Tarun','Piyush','Anjesh','Subran',],20)
num=np.random.choice([23,34,54,67,19],20)

#Using zip creating DataFrame
# a=list(zip(temp,name,num))
# DF=pd.DataFrame(data=a, columns=['temp','name','num'])
# print(DF)

#Using dictionary creating DataFrame
DF=pd.DataFrame({'Temp':temp,'Name':name,'Num':num})
# print(DF)

#Operations on DataFrame

#head()-->will display starting 5 rows
# print(DF.head())

#tail()--> will display last 5 rows
# print(DF.tail())

# print('Dimension of DataFrame',DF.shape)
# print("Columns name->>",DF.columns)
# print('\n\n')
#TO see a particular column value
# print(DF.Name)  #same as print(DF['Name'])

# print(DF['Temp'].describe())
# print(DF.info())

 