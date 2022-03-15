print("#1-----------\n")
class Sensore():
    def __init__(self, temp = 0.0):
        self.temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.temp * 1.8)

s = Sensore()
s.temp = 24.0
print(s.toFahrenheit())
print(s.__dict__)

print("#2-----------\n")
class Sensore2():
    def __init__(self, temp = 0.0):
        self.__temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.__temp * 1.8)

    def getTemp(self):
        return self.__temp
    
    def setTemp(self, t):
        if t < 0:
            t = 0;
            print("temp non permessa")
        self.__temp = t

s2 = Sensore2()
s2.setTemp(30.0)
print(s2.toFahrenheit())
s2.setTemp(-10.0)
print(s2.getTemp())

print("#3-----------\n")
class Sensore3():
    def __init__(self, temp = 0.0):
        self.__temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.__temp * 1.8)

    def getTemp(self):
        print("get")
        return self.__temp
    
    def setTemp(self, t):
        print("set")
        if t < 0:
            t = 0;
            print("temp non permessa")
        self.__temp = t

    #temp = property(getTemp, setTemp)
    temp = property()
    temp = temp.getter(getTemp)
    temp = temp.setter(setTemp)    
    

s3 = Sensore3()
s3.temp = 30.0
print(s3.temp)
s3.setTemp(-10.0)
print(s3.getTemp())
print(s3.__dict__)

print("#4-----------\n")
class Sensore4():
    def __init__(self, temp = 0.0):
        self.__temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.__temp * 1.8)

    @property
    def temperatura(self):
        return self.__temp
    
    @temperatura.setter
    def temperatura(self, t):
        if t < 0:
            t = 0;
            print("temp non permessa")
        self.__temp = t
        
s4 = Sensore4()
s4.temperatura = 12.0
print(s4.temperatura)
        