# Deze functie zet Fahrenheit om naar Celsius
def FahrenheitNaarCelsius(Farhenheit):
    res = (Farhenheit - 32) / 1.8 
    return f"De temperatuur van Fahrenheit naar Celsius is: {round(res, 1)} celsius"

# Deze functie zet Celsius om naar Fahrenheit
def CelsiusNaarFahrenheit(Celsius):
    res = (Celsius * 1.8) + 32 
    return f"De temperatuur van Celsius naar Fahrenheit is: {round(res, 1)} Fahrenheit"

# User keuze laten maken
keuze = str(input("Celsius of Fahrenheit?  "))



# Handel keuze 
if(keuze == "Celsius"):
    cel = float(input("Geeft temperatuur in celsius te omzetten naar Fahrenheit: "))
    print(CelsiusNaarFahrenheit(cel))

elif(keuze == "Fahrenheit"):
    fah = float(input("Geeft temperatuur in Fahrenheit te omzetten naar Celsius: "))
    print(FahrenheitNaarCelsius(fah))

