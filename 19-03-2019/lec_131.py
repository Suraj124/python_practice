a,b=[int(x) for x in input("Enter two  numbers : ").split()]
try:
    f=open("myfile","w")
    c=a/b
    f.write("Writing %d into file " %c)
except:
    print("Divide by zero error")
finally:
    f.close()
    print("File is closed")
print("Last statement executed")