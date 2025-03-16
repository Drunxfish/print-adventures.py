class Auto:
    def __init__(self, merk: str, kenteken: str, type: str, tank: int, kleur: str):
        self.merk = merk
        self.kenteken = kenteken
        self.type = type
        self.tank = tank
        self.kleur = kleur
    
    def start_auto(self):
        print(f"De {self.merk} {self.type} ({self.kleur}) is gestart!")


    def stop_auto(self):
        print(f"De {self.merk} {self.type} ({self.kleur}) is gestopt!")

    def check_tank(self):
        if self.tank < 10:
            print(f"De {self.merk} {self.type} moet zo spoedig mogelijk tanken! Er is nog maar {self.tank}% benzine in de tank!")
        elif self.tank > 10 and self.tank < 40:
            print(f"De {self.merk} {self.type} moet binnenkort tanken. Er zit nog maar {self.tank}% benzine in de tank!")
        else:
            print(f"{self.merk} {self.type} heeft nog voldoende benzine, namelijk {self.tank}%  !")
    

    def check_kenteken(self):
        print(f"De {self.merk} {self.type} ({self.kleur}) heeft als kenteken {self.kenteken}")



# Tijdelijke instance aanmaken en alle 4 functies gelijk uitvoeren
Auto('BMW', 'AB-342-CD', 'idk', 10, "Paars").start_auto() # 1
Auto('WMB', 'CD-243-BA', 'KDI', 20, "Oranje").stop_auto() # 2
Auto('Supra', 'EF-132-GH', 'DKI', 30, "Geel").check_kenteken() # 3
Auto("Johhny Silverhand's sporsche ", 'IJ-321-KL', 'idk', 38, "Zwart").check_tank() # 4