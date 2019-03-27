a,b=[int(x) for x in input("Enter two numbers : ").split()]
try:
    c=a/b
except ZeroDivisionError:
    print("Divide by zero is not allowd")
print("Statement after excution")