def dbl(n):
    return n**2

lst=[1,2,3,4,5]
result=list(map(dbl,lst))
print(result)

################ with lamda ##############

res=list(map(lambda x:x**2,lst))
print(res)