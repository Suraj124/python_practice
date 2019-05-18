import sys

lst=sys.argv    #return a list in which 0th element is program name remaining will be command line 
print(type(lst))    #  will be command line values
for i in lst:
    print(i)
print(len(lst))