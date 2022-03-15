from L011_cvsmod import CSV

def main():
    csv = CSV("Tab11.csv")
    nr = csv.getRowsCount()
    print("il file ha:", nr, "righe")

    print(csv)

    v = csv.getCell(1,1)
    print("cella:", v)
    
if __name__ == "__main__":
    main()