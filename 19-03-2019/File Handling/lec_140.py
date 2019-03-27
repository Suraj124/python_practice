f=open("file1.txt","w")
print("Enter a string(type @ when done writing)")
s=''
while s!='@':
    s=input()
    f.write(s+"\n")
f.close()