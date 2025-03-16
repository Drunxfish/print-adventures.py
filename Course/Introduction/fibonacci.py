
lijst = []
gebruikerInput = int(input("Hoeveel fibonacci getallen wilt u uitrekenen? "))

# controleren of het user input geset is 
if gebruikerInput != 0:
    # itereren tot het gewenste fibonacci aantal
    for i in range(0, gebruikerInput, 1):
        # 0 en 1 toevoegen in onze lijst
        if i <= 1:
            lijst.append(i)
            print(i)
        else:
            # fibonacci sequence genereren
            lijst.append(lijst[-1] + lijst[-2])
            
            # phi berekenen 
            phi = float(lijst[-1] / lijst[-2])

            # fibonacci getal en phi uitprinten
            print(f"{lijst[-1]} - phi: {phi}")





