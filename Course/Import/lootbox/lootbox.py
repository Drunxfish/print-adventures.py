import rewards

# Skin teller
legendary = epic = rare = common = 0

# 5 Skins ophalen en aantal opslaan op een variabele
for _ in range(5):
    skin = rewards.get_new_skin()
    # checken welke skin wij terug krijgen van rewards functie
    match skin:
        case "COMMON":
            common += 1
        case "RARE":
            rare += 1
        case "EPIC":
            epic += 1
        case "LEGENDARY":
            legendary += 1
    

# als de waarden niet 0 zijn dan printen wij aantal desbetreffende skin in de terminal
if common != 0:
    print(f"{common}x common")
if(rare != 0):
    print(f"{rare}x rare")
if(epic != 0):
    print(f"{epic}x epic")
if(legendary != 0):
    print(f"{rare}x legendary")

    