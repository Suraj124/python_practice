str="Suraj Yadav Suraj Yadav suraj yadav"
print(str.find("Y")) #find() return the position of alphabet or word

print(str.find("aj"))

print(str.find("Ya",(str.find("Ya")+1),len(str)))   #find("string",startIndex,EndIndex)

print(str.count("Suraj")) #count()-> Counts the frequency 

print("replace()->>"+str.replace("Suraj","Traun")) 
print("replace()->> only one string->>"+str.replace("Suraj","Tarun",1))

print("lower()->>"+str.lower())
print("upper()->>"+str.upper())
print("title()->>"+str.title())