import logging
logging.basicConfig(filename="mylogfile.log",level=logging.DEBUG)
a,b=[int(x) for x in input("Enter two  numbers : ").split()]
try:
    f=open("myfile","w")
    logging.info("Division in progress")
    c=a/b
    f.write("Writing %d into created file" %c)
except:
    print("Divide by zero error")
    logging.error("Division by zero error")
else:
    print("You have entered non zero number")
finally:
    f.close()
    print("File is closed")
print("Last statement executed")