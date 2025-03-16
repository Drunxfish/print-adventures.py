# class Dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def introduce(self):
#         print(f"My name is {self.name}, I am {self.age} years old and of {self.breed} breed")
    
#     def wouf(self, times: int):
#         print(f"{self.name} says: {times * ' Wof'}!")


# timmy = Dog('Shaco', 34, 'Mecxvare')


# timmy.introduce()
# timmy.wouf(3)
# --------------------------------------------------------------------------------------------


class ING:
    def __init__(self, name, accountNumber, amount: float):
        self.name = name
        self.accountNumber = accountNumber
        self.amount = amount

    def greet(self):
        print(f"Hello {self.name}")

    def get_amount(self):
        print(f'Current amount on your account: {round(self.amount, 2)}')
    
    def set_amount(self, transactionAmount: float, description: str):
        if float(self.amount) < 0:
            self.amount -= transactionAmount
            print(f"Transaction successful\nNew amount: {round(self.amount, 2)}\nTransaction details: {description}")
        else:
            self.amount += transactionAmount
            print(f"There is a new deposit to your account\nTransaction details: {description}\nNew amount: {round(self.amount, 2)}")
            
jorji = ING('Jorji', 'INGB93 84181239123', 393.23)
jorji.greet()
jorji.set_amount(-353, '2 uur salaris')

# --------------------------------------------------------------------------------------------

# parent klas 
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def introdcue(self):
        print(f"Hoi, ik ben {self.name} en ik ben een {self.species}")
    


# inhertiance
class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, species="Kat",)
        self.breed = breed
        self.age = age
        
    def speak(self):
        print("Meow meow meow")