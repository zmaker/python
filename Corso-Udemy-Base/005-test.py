temp = int(input("dammi la temperatura: "))

if (temp < 10):
    print("freddo")
elif ((temp >= 10) and (temp < 20)):
    print("medio")
elif ((temp >= 20) and (temp < 30)):
    print("caldo")
else:
    print("caldissimo")
    
print("ok")