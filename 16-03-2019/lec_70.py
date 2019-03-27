def calc(a,b):
    sum=a+b
    diff=a-b
    mul=a*b
    div=a/b
    return sum,diff,mul,div
result=calc(10,5)   #  In multiple return function return a tuple
print(result)
print(type(result))