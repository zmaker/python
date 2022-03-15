class Forma():
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
class Colorato():
    def __init__(self, colore):
        self.colore = colore
        
class Rettangolo(Forma):
    def __init__(self, l, w):
        super().__init__(l, w)

    def area(self):
        return self.l * self.w
    
    def __str__(self):
        return f"R({self.w}x{self.l})"

class Quadrato(Rettangolo, Colorato):
    def __init__(self, l, c):
        Rettangolo.__init__(self, l, l)
        Colorato.__init__(self, c)

    def __str__(self):
        return f"Q({self.l}) colore: {self.colore}"

r = Rettangolo(10, 24)
print(r)
q = Quadrato(15, "red")
print(q)
    
    
