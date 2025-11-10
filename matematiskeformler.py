from random import randint

a = randint(-100,100)
b = randint(-100,100)
c = randint(-100,100)   

svar1 = a * (b+c)
svar2 = a * b + a * c

print("Venstre side (svar1):", svar1)
print("Høyre side (svar2):", svar2)

print("Er de to sidene like? (True/False)", svar1 == svar2)