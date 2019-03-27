import re
p=re.compile('\w+')
res=p.findall("I was doing *** my, work at that time _")
print(res)