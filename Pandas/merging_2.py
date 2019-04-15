import pandas as pd 

DF1=pd.DataFrame({
    'city':['Lucknow','Agra','Kanpur','Delhi'],
    'temperatue':[30,23,40,33]
})

DF2=pd.DataFrame({
    'city':['Delhi','Lucknow','Agra'],
    'humidity':[33,41,23]
})

# DF=pd.merge(DF1,DF2, on='city')
# print(DF) #it will display for common values in city

# DF=pd.merge(DF1,DF2, on=['city'] , how='outer')
# print(DF) #it will display all the values for city

# DF=pd.merge(DF1,DF2, on=['city'] , how='left')
# print(DF)

# DF=pd.merge(DF1,DF2, on=['city'] , how='rigth')
# print(DF)


