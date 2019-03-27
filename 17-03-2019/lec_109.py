class Student:
    branch="CS"

    def __init__(self,name,rollNumber):
        self.name=name
        self.rollNumber=rollNumber

s1=Student("John",1)
s2=Student("Smith",2)

print(s1.branch)        #static field are commom for all objects
print(s2.branch)

print(s1.name)
print(s2.name)

print(Student.branch)       # Static field can also be accessed with help of Class name 
