# lege array(lijst)
studenten = []

# 3 random studenten appenden in de lijst
studenten.append("Jan")
studenten.append("Marika")
studenten.append("Neveli")

print("Studenten na het toevoegen:",studenten)



# st4 toevoegen op de positie index(1)
studenten.insert(1, "Datia")

# specifiek student verwijderen
studenten.remove("Jan")

# laatste item(student) verwijderen uit het lijst
studenten.remove(studenten[-1])

print("Na het insterten en toevoegen:",studenten)

# specifiek student vinden en op een variabele opslaan
marika = studenten[1]

studenten.sort()


# print hele lijst uit
print(studenten)