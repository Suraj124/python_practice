import pandas as pd 

df=pd.read_csv("weather_data.csv")
print(df)

#we can convert DataFrame to a excel file by using to_excel() method
#but you need to install openpyxl libraray

#df.to_excel('df_xl.xlsx',sheet_name='weather_data')

#To read the data of .xlsx we need read_excel() method and befoer that you need to
#insatll xlrd libraray

# df1=pd.read_excel('df_xl.xlsx')
# print(df1)

#to convert a .xlsx file to .csv
# df1.to_csv('new_csv_file.csv')
# df1.to_csv('new_csv_file_withNoIndex.csv', index=False)

# csv1=pd.read_csv('new_csv_file.csv')
# csv2=pd.read_csv('new_csv_file_withNoIndex.csv')
# print(csv1,'\n')
# print(csv2)