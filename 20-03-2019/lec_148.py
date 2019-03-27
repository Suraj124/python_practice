import re
st="Take up 2 one idea,one 455 idea 34 at a time"
res=re.split(r'\d+',st)     # + is used for one or more numbers
print(res)