from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def speake(self):
        pass
    @abstractmethod
    def food(self):
        pass
    def details(self):
        pass
class Dog(Animal):
    
    def details(self):
        print("DOG DETAILS")
    def move(self):
        print("They can walk and run")
    def speake(self):
        print("bow bow bow bow bow")
    def food(self):
        print("They can eat maximum whatever human can eat")
    
class Cow(Animal):
    
    def details(self):
        print("COW DETAILS")
    def move(self):
        print("They can walk ")
    def speake(self):
        print("ambaa ambaaa ambaaa")
    def food(self):
        print("threes and some human food")

    
animal1=Cow()
animal2=Dog()
animal1.details()
animal1.move()
animal1.speake()
animal1.food()
print("\n")
animal2.details()
animal2.move()
animal2.speake()
animal2.food()

