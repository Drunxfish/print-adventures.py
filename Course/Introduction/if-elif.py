# vraag stellen en zijn antwoord opslaan op een variabel
MagOfNiet = float(input(" \n Om rijlessen te kunnen volgen moet je minimaal 16.5 jaar zijn \n hoe oud ben jij?  "))

# controleren of de persoon ouder genoeg is
if MagOfNiet >= 16.5:
    print("Je mag beginnen met rijlessen!")
else:
    print("Helaas, jij mag nog niet beginnen met rijlessen")
