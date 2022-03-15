class Led():
    def __init__(self, colore, stato):
        self.colore = colore
        self.stato = stato
        
    def accendi(self):
        self.stato = "on"

    def spegni(self):
        self.stato = "off"
        
    def __str__(self):
        return f"Led {self.colore}: st:{self.stato}"

led1 = Led("red", "off")
print(led1)
led1.accendi()
print(led1)
led1.spegni()
print(led1)