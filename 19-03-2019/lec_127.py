from abc import abstractmethod,ABC  
class BMW(ABC):                     #All the methods here are abstract so this is interface
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):  
        pass          

class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
    
    def display(self):
        print("Cruise control is enabled")
    
    def drive(self):        
        print("abstarct mrthod -> drive() in ThreeSeries")
    def start(self):
        print("abstarct mrthod -> start() in ThreeSeries")
    def stop(self):
        print("abstarct mrthod -> stop in ThreeSeries")

class FiveSeries(BMW):
    def __init__(self,parkingAssistantEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistantEnabled=parkingAssistantEnabled
    
    def drive(self):        
        print("abstarct mrthod -> drive() in FiveSeries")
    def start(self):
        print("abstarct mrthod -> start() in FiveSeries")
    def stop(self):
        print("abstarct mrthod -> stop() in FiveSeries")

threeSeries=ThreeSeries(True,"BMW","328i",2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()
# bmw=BMW()                    #we cant not create the object of Interface

# fiveSeries=FiveSeries(True,"BMW","328i",2018)
# print(fiveSeries.parkingAssistantEnabled)
# print(fiveSeries.make)
# print(fiveSeries.model)
# print(fiveSeries.year)