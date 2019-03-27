import os,sys
if os.path.isfile("file2.txt"):
    f=open("file2.txt","r")
    s=f.read()
    print(s)
    f.close()
else:
    print("File does not exit")
    sys.exit()