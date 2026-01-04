huskeliste = []

while True:
    husk = input("Skriv inn en ting (eller 'Liste' for å se listen): ")

    if husk == "Liste":
        huskeliste.sort()
        print(huskeliste)
    else:
        huskeliste.append(husk)

        if len(huskeliste) > 10:
            print("Hei! Nå begynner listen å bli ganske lang!")
