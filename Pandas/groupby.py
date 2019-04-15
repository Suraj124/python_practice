import pandas as pd 

DF=pd.read_csv('weather_data.csv')
# print(DF)

DF_groupby_event=DF.groupby('event')

# for i in DF_groupby_event:
#     print(i)

# print(DF_groupby_event.get_group('Rain'))

# print(DF_groupby_event.describe())

# def hot_temp(x):
#     return x>30
# # DF['Hot temp']=DF['temperature'].apply(hot_temp)
# DF['Hot temp']=DF['temperature'].apply(lambda x:x>30)
# print(DF)