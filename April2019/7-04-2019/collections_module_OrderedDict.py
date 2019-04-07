from collections import OrderedDict

d={}
d['A']=1
d['B']=2
d['C']=3
d['D']=4
d['E']=5
d['F']=6
d['G']=7

print(d)

for i,j in d.items(): #In normal dictionary order is not maintained
    print(i,j)

#-------------------------------------------------#
#   OrderedDict     #
print("OrderedDict")
dd=OrderedDict() #In order dictionary order is maintained
dd['A']=1
dd['B']=2
dd['C']=3
dd['D']=4
dd['E']=5
dd['F']=6
dd['G']=7

for k,v in dd.items():
    print(k,v)

#--------------------------------------------------#

d1={}
d1['A']=1
d1['B']=2
d2={}
d2['B']=2
d2['A']=1

print(d1==d2)   #True

#-----------------------------------------------------#

dd1=OrderedDict()
dd1['A']=1
dd1['B']=2
dd2=OrderedDict()
dd2['B']=2
dd2['A']=1

print(dd1==dd2)