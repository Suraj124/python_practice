x=123
def display():
    x=789
    print(x)
    print(globals()['x'])

print(x)
z=display       # Assigning function to a vraible
z()
z()