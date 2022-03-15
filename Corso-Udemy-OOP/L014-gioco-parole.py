from random import randint

class Dictionary():
    def __init__(self):
        self.count = 0
        with open("L014-words.txt", 'r') as f:
            line = f.readline()
            while True:
                self.count += 1
                line = f.readline()
                if not line:
                    break
        #print(self.count)
    
    def sort(self, minlen):
        word = ""
        lw = 0
        while lw < minlen:
            n = randint(0, self.count-1)
            with open("L014-words.txt", 'r') as f:
                for i, line in enumerate(f):
                    if i == n:
                        word = line.strip().upper()
                        break
            lw = len(word)
        return word

class HangedMan():
    
    MAXLEN = 6
    
    def __init__(self):
        self.dict = Dictionary()
        self.letters = []
    
    def play(self):
        #estraggo una parola a caso dal dizionario
        self.secret = self.dict.sort(self.MAXLEN)
        print(self.secret)
        #stampo numero di lettere da indovinare
        print("lettere: ", len(self.secret))
        self.attempt = 0
        
        while True:
            #stampo la parola mascherata
            (w, c) = self.masked()
            print(w)
            if c == len(self.secret):
                print("Complimenti!!")
                break
            #chiedo una lettera
            ch = input("che lettera? ").upper()
            #verifico se la lettera è nella parola
            if ch in self.secret:
                #salvo la lettera in una lista
                print("presente!")
                self.letters.append(ch)
            else:
                #non ho indovinato
                print("non presente!")
                #segno l'errore o numero di tentativi
                self.attempt += 1
                t = self.MAXLEN - self.attempt
                print("hai ancora: ", t, "tentativi")
            
            #se ho fatto troppi sbagli termino
            if self.attempt == (self.MAXLEN - 1):
                #stampo la parola e termino
                print("hai perso! La parola era: ", self.secret)
                break
            
            
    def masked(self):
        s = ""
        c = 0
        for ch in self.secret:
            if not ch in self.letters:
                s += "_ "
            else:
                s += ch+" "
                c += 1
        return s, c

g = HangedMan()
g.play()
