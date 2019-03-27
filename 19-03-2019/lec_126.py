from abc import abstractmethod,ABC  #notice here importing abc module for Abstraction
class BMW(ABC):                     #notice here BMW inheriting ABC class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")
    @abstractmethod
    def drive(self):  # we can not define the body of abstact method in abstract class
        pass          # the classes which inherti the abstract class must over ride it and give definition

class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
    def display(self):
        print("Cruise control is enabled")
    
    def drive(self):         #defining the body for abstract method
        print("Drive class is driven")

class FiveSeries(BMW):
    def __init__(self,parkingAssistantEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistantEnabled=parkingAssistantEnabled
    
    def drive(self):        #defining the body for abstract method
        print("Drive class is driven")

threeSeries=ThreeSeries(True,"BMW","328i",2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()
# bmw=BMW()                    #we cant not create the object of Abstract class

# fiveSeries=FiveSeries(True,"BMW","328i",2018)
# print(fiveSeries.parkingAssistantEnabled)
# print(fiveSeries.make)
# print(fiveSeries.model)
# print(fiveSeries.year)