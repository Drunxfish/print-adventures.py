# het jaar vragen aan de gebruiker
schrikkeljaar = int(input("Vul het jaar in: "))


# controleren of het gegeven jaar een schrikkel jaar is 
if(schrikkeljaar % 4 != 0):
    print(f"{schrikkeljaar} is geen schrikkeljaar")
elif(schrikkeljaar % 4 == 0 and schrikkeljaar % 100 != 0):
    print(f"{schrikkeljaar} is wel een schrikkel jaar")
elif(schrikkeljaar % 4 == 0 and schrikkeljaar % 100 == 0 and schrikkeljaar % 400 == 0):
    print(f"{schrikkeljaar} is wel een schrikkeljaar")
else:
    print(f"{schrikkeljaar} is geen schrikkeljaar")
