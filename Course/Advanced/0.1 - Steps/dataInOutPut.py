import time, sys

def find_goal_total(filename):
    with open(filename, 'r') as data:
        goal_total = 0
        for row in data:
            split_data = row.split(',')
            goal_total += int(split_data[2]) + int(split_data[3])
            print(f"Er is in totaal {goal_total} keer gescoord")


def find_away_wins(bestandnaam):
    with open(bestandnaam) as data:
        away_wins = 0
        teams = []
        for row in data:
            splitted = row.split(',')
            if int(splitted[2]) > int(splitted[3]):
                away_wins += 1
                teams.append(splitted[0])
        return teams, away_wins # namen
    


while True:
    try:
        file = str(input("Geef de bestands naam op:  "))
        if not file or ".txt" not in file:
            raise EOFError
        uitspelende_teams, totaal = find_away_wins(file) # Geef input
    except EOFError:
        print("Onjuiste of lege input")
        pass
    except FileNotFoundError:
        print("Bestand bestaat niet!")
        pass  
    except KeyboardInterrupt:
        print("\nProgramma handmatig afgesloten")
        sys.exit(0)
    else: 
        print(f"Er hebben {totaal} uitspelende teams gewonnen.")   
        print(f"Dit waren: {', '.join(uitspelende_teams)}") # data op nette manier formateren    
        break
    finally:
        print(f"Programma beeingd om: {time.strftime("%H:%M:%S")}")
sys.exit(0)

# find_goal_total('uitslagen.txt')
