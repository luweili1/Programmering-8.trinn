import random

elever = [
    "Lawin", "Anders", "Leona", "Tiantian", "Henrik", 
    "Stevan", "Aarash", "Victoria", "Magnus", "Kristi", 
    "Sharanya", "Vegar", "Manha", "Nora", "Katharina", 
    "Benjamin", "Nima", "Sebastian", "Sigrid", "Minh", 
    "Fedor", "Theodor", "Zitong", "Advika", "Marius", 
    "David", "Oscar"
]

random.shuffle(elever)
grupper = [elever[i:i+3] for i in range(0, len(elever), 3)]


def print_grupper(grupper):
    for idx, gruppe in enumerate(grupper, 1):
        print(f"Gruppe {idx}:")
        for navn in gruppe:
            print(f"+{'-'*(len(navn)+2)}+")
            print(f"| {navn} |")
            print(f"+{'-'*(len(navn)+2)}+")
        print("\n")

print_grupper(grupper)

