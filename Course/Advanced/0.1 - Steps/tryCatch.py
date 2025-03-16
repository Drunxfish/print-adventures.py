import sys, time


def checkNegative(waarde):
    if float(waarde) < 0:
        raise ValueError



# Try/except
while True:
    try:
        number = float(input("vul uw favoriete nummer in: "))
        checkNegative(number)
    except ValueError:
        print("Het moet echt een getal zijn !")
        pass
    else:
        if number >= 0:
            print(f"Uw favoriete nummer is {number}")
            break
        else: 
            raise ValueError
    finally:
        print(f"""
         _______________________________
        |                               |
        |        Operatie voltooid      |
        |        Duur: {time.strftime("%H:%M")}            |
        |_______________________________|
          """)
sys.exit(0)

