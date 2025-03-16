# input vragen aan user
speler1 = int(input("Wat is de score van speler een?: "))
speler2 = int(input("Wat is de score van speler twee?: "))


# Score vergelijking
if(speler1 > speler2):
        print("Speler een heeft gewonnen!")
elif(speler2 > speler1):
        print("Speler twee heeft gewonnen!")
else:
    print("Het is gelijkspel!")