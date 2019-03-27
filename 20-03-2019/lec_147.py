import re
st="Take up one idea,one idea at a time"
result=re.findall(r'o\w',st)
print(result)

res=re.match(r'T\w',st)
# print(res)   res is object
print(res.group())