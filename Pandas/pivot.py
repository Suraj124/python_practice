import pandas as pd 

DF=pd.read_csv('weather_data.csv')

# print(DF.pivot_table(values='temperature', index='event', aggfunc='mean'))

# print(DF)
# print('\n')
# print(DF.pivot_table(columns='temperature'))

#help

print(help(pd.DataFrame.pivot_table))
