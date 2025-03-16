# VRAAG 1: Hoeveel doelpunten zijn er in totaal bij wedstrijden gemaakt tussen Ajax en Feyenoord?
def totaal_aantal_doelpunten(bestand):
    with open(bestand, "r") as data:
        totaal_aantal = 0
        for rij in data:
            split_data = rij.split(",")
            totaal_aantal += int(split_data[3]) + int(split_data[4])
    print(f"VRAAG 1: Er zijn in totaal {totaal_aantal} doelpunten gescoord gemaakt.")



# VRAAG 2: Hoeveel doelpunten heeft Feyenoord gescoord in hun uitwedstrijden bij Ajax?
def totaal_winnende_doelpunten_feyenoord(bestand):
    with open(bestand, "r") as data:
        totaal = 0
        for rij in data:
            split_data = rij.split(",")
            if str(split_data[1]).lower() == 'ajax' and str(split_data[2]).lower() == 'feyenoord':
                totaal += int(split_data[4])
    print(f"VRAAG 2: Feyenoord heeft {totaal} keren gescoord in de ArenA.")



# VRAAG 3: Op welke datum hield Ajax voor het eerst de nul in de ArenA en incasseerde het dus geen enkel tegendoelpunt?
def datum_van_eerste_nul(bestand):
    datum = ''
    with open(bestand, "r") as data:
        for rij in data:
            split_data = rij.split(",")
            if ((str(split_data[2]).lower() == "ajax" and int(split_data[3]) == 0) or (str(split_data[1]).lower() == "ajax" and int(split_data[4]) == 0)):
                datum = split_data[0]
                break
    print(f"VRAAG 3: Ajax hield voor het eerst op {datum} de nul in de ArenA tegen Feyenoord.")



# functies uitroepen 
totaal_aantal_doelpunten("klassieker.txt")
totaal_winnende_doelpunten_feyenoord("klassieker.txt")
datum_van_eerste_nul("klassieker.txt")



