class Rettangolo():
    def __init__(self, l, w):
        self.w = w
        self.l = l
        
    def area(self):
        return self.w * self.l

class Quadrato(Rettangolo):
    def __init__(self, l):
        super().__init__(l, l)

r = Rettangolo(10, 20)
print(r.area())
q = Quadrato(15)
print(q.area())