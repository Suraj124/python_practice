# lst=[1,2,3,4,5,6,7,8,9]

# res=filter(lambda x:x%2==0,lst)
# print(res)  #return the memoery location of filter object

res=list(filter(lambda x:x%2==0,range(1,21)))
print(res)
