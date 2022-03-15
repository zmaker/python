class Led:
    def __init__(self):
        print("init")
        self.marca = "superlight"
        self.colore = "verde"
        self.diametro = 5


led1 = Led()
led2 = Led()

print(led1)
print(led2)

print(led1.marca)
print(led1.colore)
led1.colore = "rosso"
print(led1.colore)

print(led2.colore)