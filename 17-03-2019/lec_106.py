class cource:

    def __init__(self,name,rating):
        self.name=name
        self.rating=rating
    def average(self):
        numberOfRatings=len(self.rating)
        avg=sum(self.rating)/numberOfRatings
        print("Average rating of",self.name,"is",avg)

obj=cource("Java Course",[2,3,5,4,5])
print(obj.name)
print(obj.rating)
obj.average()

obj2=cource("Python",[5,5,5,5])
print(obj2.name)
print(obj2.rating)
obj2.average()