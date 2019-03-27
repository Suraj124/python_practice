import re
st="Take up one idea.One idea at a time"

# res=re.search(r'^o\w',st) #This will gove error as first word does not start with o
res=re.search(r'^T\w+',st)
print(res.group())

