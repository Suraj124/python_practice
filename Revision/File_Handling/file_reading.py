f=open('example.txt','r')
print(f.read(5))
print(f.read(10))   # current file pointer is at 10
print(f.tell())
print(f.read(5))    # current file pointer is at 15
print(f.tell())
f.seek(0)           # current file pointer is at 0
print(f.read(5))
f.close()