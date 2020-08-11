# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class clsUser:
    #constructor
    def __init__(self, iName,iAage):
        self.username=iName
        self.userage =iAage

    def greeting(self):
        print(f'hi {self.username}, you are {self.userage} years\' old')



class clsCustomer(clsUser):
    def __init__(self, iName,iAage):
        self.username=iName
        self.userage =iAage
        self.balance =0
    def setBalance(self,iBalance):
        self.balance = iBalance
    def showBalance(self):
        print(f'your balance is {self.balance}')