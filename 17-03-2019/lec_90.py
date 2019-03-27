def decor(fun):
    def inner():
        res=fun()*2
        return res
    return inner
@decor                  #  After @ there is name of the decorator function here it is decor
def num():
     return 5

print(num())