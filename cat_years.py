# 1. Be brukeren skrive inn antall menneskeår
menneskeår = int(input("Hvor gammel er katten i menneskeår? "))

# 2. Regne om til katteår
if menneskeår == 1:
    katteår = 15
elif menneskeår == 2:
    katteår = 15 + 9               # = 24
else:
# De første to årene gir alltid 24 katteår sammen, derfor trekker vi fra to og teller de årene etter 2 år.
    katteår = 24 + (menneskeår - 2) * 4

# 3. Skriv ut resultatet
print("Katten er", katteår, "katteår gammel.")

