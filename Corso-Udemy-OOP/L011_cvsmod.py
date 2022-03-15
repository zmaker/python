import os.path

class CSV():
    def __init__(self, filename):
        self.filename = filename
        if os.path.isfile(self.filename):
            self.file = open(self.filename)
            self.lines = list()
            self.rows = 0
            line = self.file.readline()
            self.lines.append(Row(line))
            while line:
                line = self.file.readline()
                self.lines.append(Row(line))
            
        else:
            print("file non esiste")
        
    def getRowsCount(self):
        return len(self.lines)
    
    def getRow(self, n):
        return self.lines[n]

    def getCell(self, r, c):
        rw = self.getRow(r)
        c = rw.getCell(c)
        return c.getValue()
    
    def __str__(self):
        txt = f"CSV File - {self.filename}\n"
        for r in self.lines:
            txt += str(r) + "\n"
        return txt

class Row():
    def __init__(self, txt):
        items = txt.split(sep=",")
        self.cells = []
        for el in items:
            self.cells.append(Cell(el))
    
    def getCell(self, n):
        return self.cells[n]
    
    def __str__(self):
        txt = ""
        for el in self.cells:
            txt += str(el)
        return txt

class Cell():
    def __init__(self, txt):
        self.value = txt.strip().replace('\n', '')
    
    def getValue(self):
        return self.value

    def __str__(self):
        s = self.value.ljust(12)
        return s
        

if __name__ == "__main__":
    print("non eseguibile")