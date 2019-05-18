def display(fun):
    return "hello "+fun()
def name():
    return "Smith"
print(display(name))    #passing name function in display function