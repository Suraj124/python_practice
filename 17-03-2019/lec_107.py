class Programmer:

    def setName(self,n):
        self.name=n

    def setSallery(self,sal):
        self.sallery=sal

    def setTechnologies(self,tech):
        self.technologies=tech


    def getName(self):
        return self.name

    def getSallery(self):
        return self.sallery
    def getTechnologies(self):
         return self.technologies

p1=Programmer()
p1.setName("Smith")
p1.setSallery(1000)
p1.setTechnologies(["Java","HTML and CSS","Python"])

print(p1.getName())
print(p1.getSallery())
print(p1.getTechnologies())
