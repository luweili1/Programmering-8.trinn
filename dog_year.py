menneskeår = int(input("Hvor gammel er hunden i menneskår? "))

if menneskeår == 1:
    hundeår = 15

elif menneskeår == 2:
    hundeår = 15 + 9

else:
    hundeår = 24 + (menneskeår-2)*5


print ("En hund som er", menneskeår, "er:", hundeår, "år gammel i hundeår")