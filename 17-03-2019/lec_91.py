def howareyou(fun):
    def inner(n):
        st=fun(n)+" How are you ?"
        return st
    return inner
@howareyou
def hello(name):
    return "hello "+name

print(hello("Smith"))