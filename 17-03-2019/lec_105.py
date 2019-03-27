class cource:

    def __init__(self,name,rating):
        self.name=name
        self.rating=rating

obj=cource("Java Course",[2,3,5,4,5])
print(obj.name)
print(obj.rating)
obj2=cource("Python",[5,5,5,5])
print(obj2.name)
print(obj2.rating)