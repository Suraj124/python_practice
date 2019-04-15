import numpy as np
import pandas as pd 

Temp=np.random.randint(10,50,20)
Name=np.random.choice(['Suraj','Tarun','Piyush','Anjesh','Subran',],20)
Num=np.random.choice([1,3,5,8,0],20)

DF=pd.DataFrame({'Temp':Temp,'Name':Name,'Num':Num},columns=['Temp','Name','Num'])

#set_index()-->used to set index

# print('Before')
# print(DF.set_index('Temp'))  #Change in the index of DataFrame is temporary if we print orginal DF then index is deafult i.e with 0 to n
# print('\n')
# print("ORGINAL")
# print(DF)
# print("After")
#TO overcome this problem we use inplace=True in set_index()
DF.set_index('Temp', inplace = True)
print('\n')
print("ORIGINAL")
print(DF)

#sort_index()--> Index wise sorting
print(DF.sort_index(axis=0, ascending=False)) #inplace=False

#sort_values()-->Sorting on the basis of passed column
print('Sorting on the basis of Name')
print(DF.sort_values(by='Name', ascending=False)) #inplace=False
print(DF.sort_values(by='Name', ascending=True)) #inplace=False

#drop()
print('\n')
    
print('Droping Num columns')
print(DF.drop(['Num'],axis=1)) #inplace=False