from abc import ABC,abstractmethod

class Car(ABC):
    def __init__(self,b,m,y):
        self.brand=b
        self.model=m
        self.year=y
    @abstractmethod
    def car_details(self):
        pass
    def sunroof(self):
        pass
class Hatchback(Car):
    def car_details(self):
        print(f"Brand of the car is {self.brand}")
        print(f"model of the car is {self.model}")
        print(f"year of the car is {self.year}")
    def sunroof(self):
        print("not having this feature")
class Suv(Car):
    def car_details(self):
        print(f"Brand of the car is {self.brand}")
        print(f"model of the car is {self.model}")
        print(f"year of the car is {self.year}")
    def sunroof(self):
        
        print(" having this feature")
    
car1=Hatchback("Maruthi","Alto",2022)
car2=Suv("Mahindra","Mahindra XUV 3XO",2024)


car1.car_details()
car1.sunroof()
car2.car_details()
car2.sunroof()
