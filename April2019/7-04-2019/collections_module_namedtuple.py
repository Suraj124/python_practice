from collections import namedtuple

Dog=namedtuple('Dog','name color age')

d=Dog(name='Hulk',color='Brown',age=1)

print(d)
print("Age",d.age)
print('Age',d[2])

for i in d:
    print(i)
#------------------------------------------#
Cat=namedtuple('Cat','name age fur color')

c=Cat(name='Fuzzy',age=2,fur=False,color='Gray')

for i in c:
     print(i)
#------------------------------------------#