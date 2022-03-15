class Math():

    @staticmethod
    def pi():
        return 3.14
    
    @staticmethod
    def sum(a, b):
        return a+b

n = Math.pi()
print(n)
n = Math.sum(10, 20)
print(n)

class Car():
    def __init__(self, targa, matricola):
        self.targa = targa
        self.__matricola = matricola

c = Car("BC313", "1214234125354312")
print(c.targa)
#print(c.__matricola)
c.__matricola = "12541524"
print(c.__matricola)

print(c.__dict__)

class Car2():
    def __init__(self, targa, matricola):
        self.targa = targa
        self.__matricola = matricola
        
    def getMatricola(self):
        return self.__matricola

    def setMatricola(self, m):
        self.__matricola = m

c = Car2("BC313", "1214234125354312")
c.setMatricola("32773777734777377")
print(c.getMatricola())

