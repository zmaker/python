class Auto():
    def __init__(self, color, year):
        self.color = color
        self.year = year
        
    def setSpeed(self, speed):
        self.speed = speed
        
    def beep(self, sound):
        return f"emette: {sound}"
    
class Fiaz500(Auto):
    #override di beep()
    def beep(self, sound="Biiuiiip!"):
        return f"500 suona così: {sound}"
        

class Perrari(Auto):
    def guidaSportiva(self, stato):
        self.sport = stato

a = Perrari("rosso", 1995)
b = Fiaz500("gialla", 1970)

print(a.beep("hoonk"))
print(b.beep("bip bip"))

print("e' una Perrari: ", isinstance(a, Perrari))
print("e' una Perrari: ", isinstance(b, Perrari))
print("e' una 500: ", isinstance(a, Fiaz500))

print(b.beep())

a.guidaSportiva("on")



