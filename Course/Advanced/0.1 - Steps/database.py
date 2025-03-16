# Les 4B - Databases
import sqlite3


# connectie met de database, maakt db als het niet bestaat
connect = sqlite3.connect('weather.db')

# brug tussen py and sql
cursor = connect.cursor()

# data selecteren en fetchen
cursor.execute("SELECT * FROM temperature")
data = cursor.fetchall()


# data weergeven
with open('metingen.txt', 'w') as file:
    for temp in data:
        file.write(f"Op {temp[0]} was de temperatuur {temp[1]} graden\n")



# queries opslaan en verbinding sluiten
# connect.commit()
connect.close()





