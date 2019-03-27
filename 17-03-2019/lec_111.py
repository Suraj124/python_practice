class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    
    class Engine:
        def __init__(self,E_num):
            self.E_number=E_num
        
        def start(self):
            print("Engine Started")

# Car("Audi",1999).Engine(1234).start()
c=Car("BMW",1995)
e=c.Engine(1234)
e.start()
        
