num=int(input("Enter a number : "))
try:
    assert num%2==0,"Number is not even"
    print("Number is even ")
except AssertionError as obj:
    print(obj)
print("Last statement")