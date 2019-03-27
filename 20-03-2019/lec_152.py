import re
st="Yesterday was 19-03-2019 and today is 20-03-2019"
res=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',st)
print(res)