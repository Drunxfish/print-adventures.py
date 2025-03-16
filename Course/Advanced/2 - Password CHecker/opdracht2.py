import time, sys

uppercase_used = False
number_used = False
eight_digits_used = False


def check_password(x: str):
    global uppercase_used
    global number_used
    global eight_digits_used
    for char in x:
        if char.isupper():
            uppercase_used = True
        elif char.isnumeric():
            number_used = True
    if len(x) >= 8 and eight_digits_used == False:  # <-- optimatisatie :D
        eight_digits_used = True

    if all([uppercase_used, number_used, eight_digits_used]):
        return True
    else:
        raise ValueError("Het wachtwoord voldoet niet aan de gestelde eisen!")


while True:
    try:
        inp = str(input("Wat is het wachtwoord? "))
        check_password(inp)
    except ValueError as e:
        print(e)
        pass
    except KeyboardInterrupt:
        print("\nHet programma is handmatig afgesloten....\n")
        sys.exit(0)
    else:
        print("\nWachtwoord is zonder problemen ingesteld!")
        break
    finally:
        print(f"Finally het statement geprint op {time.strftime("%H:%M:%S")}!\n")
    print(
        "---------------------------------------------------"
    )  # <--- voor de netheid in de terminal :3

sys.exit(0)
