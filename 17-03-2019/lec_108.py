class Customer:

    def __init__(self):
        self.name="William"
        self.age=23
        self.gender="Male"
        self.mobile_Num=1234567890
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.mobile_Num)

# Customer().display()
c1=Customer()
c1.display()