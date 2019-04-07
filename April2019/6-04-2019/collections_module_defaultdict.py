from collections import defaultdict
d={}
print(d)

d={'k1':1,'k2':2}
print(d)

print(d['k2'])
# print(d['k3'])  #raise an error

#now we use defaultdict

dd=defaultdict(lambda:0)
print(dd['one']) #key which is not present in the dictionary it that key will assign with default value
dd['two']=2
print(dd['three'])
for i in dd.items():
    print(i)
