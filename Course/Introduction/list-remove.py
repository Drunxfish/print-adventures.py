# List van strings (tekst)
listA = ["Item 1", "Item 2", "Item 3"]
print(listA)

# Voeg Item 4 aan einde van de list toe:
listA .append("Item 4")
print(listA)

# Verwijder het tweede item uit de list.
listA.remove("Item 2")
print(listA)

# Tel hoeveel keer een item voorkomt in de list. Geef deze waarde terug.
itemCount = listA.count("Item 1")
print(f"Item 1 komt {itemCount} keer voor in listA")
listA.append("Item 1")
listA.append("Item 1")
listA.append("Item 1")
print(listA)
print(f"Item 1 komt {listA.count('Item 1')}, keer voor in listA")


# Verwijder alles uit de lijst. (Maak de lijst leeg.)
listA.clear()
print(listA)

print("===================================================")