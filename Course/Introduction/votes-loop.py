# variabeles om stemmen op te tellen
fred = 0
tim = 0

# stemmen optellen zolang de user het beeindigd met "UITSLAG"
while True:
    Wie = str(input("Op wie wil je stemmen? Frederiek of Tim  "))
    if Wie.isupper and Wie == "UITSLAG":
        # 'break' zal ervoor zorgen dat na dat user UITSLAG schrijft als antwoord-
        # - deze whike loop breekt oftewel stopt
        break
    elif Wie.lower() == "frederiek":
        fred += 1
    elif Wie.lower() == "tim":
        tim += 1

# resultaat controleren
if tim > fred:
    print("Tim heeft gewonnen! ")
elif fred > tim:
    print("Tim heeft gewonnen")
elif fred == tim:
    print("Gelijk aantal stemmen")


