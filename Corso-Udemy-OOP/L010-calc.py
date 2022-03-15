from L010_calcmod import Calc
from sys import argv

def main():
    if not len(argv) == 4:
        print("parametri non corretti! usare: calc a + b")        
    else:
        mycalc = Calc()
        mycalc.setOperando1(int(argv[1]))
        mycalc.setOperazione(argv[2])
        mycalc.setOperando2(int(argv[3]))
        v = mycalc.getResult()
        print(mycalc)
    
if __name__ == "__main__":
    main()