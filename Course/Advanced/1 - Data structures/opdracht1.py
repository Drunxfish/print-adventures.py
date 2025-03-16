from faker import Faker
import random as rand

# ----------------------
# --------Deel 1--------
# ----------------------
aantal = int(input("Hoeveel namen wilt u?"))
namen = []
fake = Faker()

for i in range(aantal):
    namen.append(fake.name())



# ----------------------
# --------Deel 2--------
# ----------------------
mijnSet = set()

def list_checker(list):
    for item in list:
        if item.startswith("C"):
            mijnSet.add(item)

list_checker(namen)
        



# ----------------------
# --------Deel 3--------
# ----------------------
mijnList = list(mijnSet)


if mijnList:
    print(f"Lengte van de lijst: {len(mijnList)}\nWillekeurige naam: {rand.choice(mijnList)}")
else:
    print("Er zijn geen namen die beginnen met een C")


# ----------------------
# --------Deel 4--------
# ----------------------
persoon = {
    'Name' : 'Courtney Gray MD',
    'Age' : 29,
    'City' : fake.city(),
    'Postal Code' : fake.postalcode(),
    'Admin' : False
}

print(persoon.items())


# -----------------------
# --------The end :D ----
# -----------------------