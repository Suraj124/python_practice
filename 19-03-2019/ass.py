class Patient:
    def setId(self,ID):
        self.id=ID
    def getId(self):
        return id

    def setName(self,NAME):
        self.name=NAME
    def getName(self):
        return name

    def setSsn(self,SSN):
        self.ssn=SSN
    def getSsn(self):
        return ssn

p=Patient()
p.setId(123)
p.setName("Smith")
p.setSsn(9080)

print(p.getId())
print(p.getName())
print(p.getSsn())