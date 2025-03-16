# functie die som van twee getallen retourneert 
def Sommetje():
    # getallen vrange
    getal1 = int(input("Geef eerste getal: "))
    getal2 = int(input("Geef tweede getal: "))

    # resultaat retourneren
    return f"De som van {getal1} en {getal2} is {getal1 + getal2}"

# functie uitvoeren en uitprinten
print(Sommetje())