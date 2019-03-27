import re
st="Take up one idea.One idea at a time"
result=re.search(r'o\w',st)
print(result.group())