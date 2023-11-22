#Adding an abstraction module for Python (Abstract Base Classes)
from abc import ABC, abstractclassmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        @abstractclassmethod
        def make_sound(self):
            pass
        
        def introduce(self):
            print(f"I am {self.name}, {self.age} years old.")
            
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
        
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        def start_engine(self):
            print(f"The {self.barand}. {self.model}'s engine is running")

# Examples of using classes            
if __name__ == "__main__":
    # Here we use the Animal calss - Encapsulation
    #animal = Animal("Generic Animal", 5) # Here we have an error, because now Animal Class is abstracted
    #animal.introduce()
    
    # Using Dog class who extend Animal class
    dog = Dog("Buddy", 3)
    dog.introduce()
    dog.make_sound()
    
    #Using Cat class who extend Animal Class
    cat = Cat("Whiskers", 2)
    cat.introduce()
    cat.make_sound() #This is polymorphism, make different from every under class
    
    #Using Car class who doesn't extend Animal class
    car = Car("VW", "Golf")
    car.start_engine()