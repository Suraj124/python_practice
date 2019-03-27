def decor(fun):
    def inner():
        res=fun()*2
        return res
    return inner

def num():
    return 5
result=decor(num)
print(result())