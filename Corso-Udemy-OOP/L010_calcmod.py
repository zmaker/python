class Calc():
    def __init__(self):
        self.result = 0
        self.operazione = "+"

    def setOperando1(self, n):
        self.op1 = n
    
    def setOperazione(self, op):
        self.operazione = op
    
    def setOperando2(self, n):
        self.op2 = n
    
    def getResult(self):
        self.calcola()
        return self.result

    def __str__(self):
        return f"{self.op1} {self.operazione} {self.op2} = {self.result}"
    
    def calcola(self):
        if self.operazione == "+":
            self.result = self.op1 + self.op2;
        elif self.operazione == "-":
            self.result = self.op1 - self.op2;
        elif self.operazione == "x":
            self.result = self.op1 * self.op2;
        elif self.operazione == "/":
            self.result = self.op1 / self.op2;

if __name__ == "__main__":
    print("file non eseguibile")