tpl=(12)        #if we give single  element in the tupple then type of tupple will be integer
print(type(tpl))

tpl1=(12,)      #but if we give comma after the single element then type tupple will be tupple
print(type(tpl1))

tpl2=(12,23,12,"Python" ,-90,-23,12,"Programming")
print(tpl2)

print(tpl2*2)       #repeat the tupple

print(tpl2.count(12))
print(tpl2.index("Programming"))
