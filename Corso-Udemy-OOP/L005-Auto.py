class Auto:
    marca = "supercar"
    
    def __init__(self, colore, targa):
        self.colore = colore
        self.targa = targa
        self.carburante = 0
        self.x = 0
    
    def __del__(self):
        print("bye")
        
    
    def __str__(self):
        return f"[{self.targa}] {self.colore} - x:{self.x} - f:{self.carburante}"
 
    def addCarburante(self):
        self.carburante += 1
        if self.carburante > 10:
            self.carburante = 10

    def marcia(self):
        if self.carburante > 0:
            self.x += 1
            self.carburante -= 1
            return True
        else:
            return False
        
    def getCarburante(self):
        return self.carburante
    
    def setCarburante(self, c):
        self.carburante = c

    
a1 = Auto("rossa", "AB123AB")
print(a1)

for i in range(10):
    a1.addCarburante()
    
print(a1)
print("partenza")
while a1.marcia():
    print(a1)
print("siamo fermi")

