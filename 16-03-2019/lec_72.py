x=123
def display():
    x=789
    print(x)
    print(globals()['x'])   #Accessing global variable

print(x)
display()