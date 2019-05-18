f=open('ex.txt','r')
#print(f.read())

# f.seek(0)
# for line in f:
#     print(line)

print(f.readline())     #readline() method to read individual lines of a file.
print(f.readline())     #This method reads a file till the newline, including the newline character.

print(f.readlines()) #The readlines() method returns a list of remaining lines of the entire file.
                     #All these reading method return empty values when end of file (EOF) is reached.
f.close()