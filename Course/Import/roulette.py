def Roulette():
    # dit zullen we gebruiken om willekeurige getal tussen 0-36 te genereren
    import random


    # standard aantal chips en dictionary waar wij de inzetten gaan opslaan
    chips = 10
    inzetten = {}

    # welkom bericht
    print(f"Welkom casino RIEN , Je begint met {chips} chips")

    # zolang de speler meer dan 0 chips heeft kan hij spelen
    while chips > 0:
        # als de user genoeg chips heeft dan kan hij verder
        while chips > 0:
            # inzet vragen
            inzet = input("Zet je inzet tussen 0 - 36  (of typ STOP om te stoppen met het Inzetten)")

            # doorgaan met het inzetten?
            if str(inzet.lower()) == "stop" and len(inzetten) >= 1:
                break

            # als speler geen getal invoert dan terug plaatsen naar boven*
            elif not inzet.isdigit():
                print("Kies een getal")
                continue

            # als speler ergens anders probeert te inzetten dan toegestaan dan terug plaatsen naar inzet input
            if not 0 <= int(inzet) <= 36:
                print("Kies Tussen: 0 en 36, niet meer niet minder")
                continue

            # input omzetten naar int
            inzet = int(inzet)

            # controleren of inzet al bekend is in dictionary en aantal chips gezet ophogen met 1
            if inzet in inzetten:
                inzetten[inzet] += 1
            # als inzet nog niet is bekend dan toekenen
            else:
                inzetten[inzet] = 1

            # elke inzet kost 1 chip dus dat wordt afgetrokken
            chips -= 1
            
        # klaar met inzetten
        print("""--------------------\nrien ne va plus\n--------------------""")


        # willekeurige getal tussen 0 - 36
        winnendNummer = random.randint(0,36)

        # checken of de player gewonnen heeft
        # winnenNummer loopen in de dictionary tot een match
        if winnendNummer in inzetten:

            # als match gevonden is aantal chips gezet op de match vermenigvuldigen op 35 chips(cadeau)
            totaal = inzetten[winnendNummer] * 35
            chips += totaal
            print(f"Wohooo Je hebt {totaal} chips gewonnen \nNieuwe aantal Chips: {chips}\n")

            # waarden terug zetten naar 0
            totaal = 0
            inzetten = {}
        # speler laten weten dat ze verloren hebben
        else:
            print(f"Helaas, je hebt verloren\nWinnende nummer: {winnendNummer}\n")
            inzetten = {}
    # als de speler geen chips meer heeft dan wordt het spel gesloten.
    if chips <= 0: 
        print("\nJe hebt geen chips meer om te spelen\nGAME OVER")
        return

# spel beginnen
Roulette()
