from functools import reduce #import functools
lst=[3,2,7,4,9,6]

print("Sum of list is : ")
sum=reduce(lambda a,b:a+b,lst)
print(sum)

print("Highest among list is : ")
high=reduce(lambda a,b:a if a>b else b,lst)
print(high)