import random

n = int(input("quanti numeri? "))

numeri = []
for i in range(n):
    nc = random.randint(0,100)
    numeri.append(nc)

input("vuoi vedere i numeri? ")

for el in numeri:
    print(el, end=" ")