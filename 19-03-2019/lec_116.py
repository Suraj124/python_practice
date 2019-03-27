class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
class FiveSeries(BMW):
    def __init__(self,parkingAssistantEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistantEnabled=parkingAssistantEnabled

threeSeries=ThreeSeries(True,"BMW","328i",2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

fiveSeries=FiveSeries(True,"BMW","328i",2018)
print(fiveSeries.parkingAssistantEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)