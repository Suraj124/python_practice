lst=[1,2,3,4,5,6,7,8,9]
print(type(lst))

b=bytes(lst)        
print(type(b))
print(b)
# b[2]=22   we can't change values in bytes

b1=bytearray(lst)
print(type(b1))
b1[2]=0     #we cna chnage the bytearray
print(b1)

#NOTE :- we can not perform slicing in bytes and bytesarray