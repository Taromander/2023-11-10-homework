print("Hello World")
class Person:
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Name:{self.name}\nAge = {self.age}\nPosition:{self.position}"

p1 = Person("John",36,"Convinient-store-clerk")
print(p1)

p2 = Person("Sue",22,"Student")
print(p2.__dict__)    

p3 = Person("Bo-jun",69,"None")
print(p3)
