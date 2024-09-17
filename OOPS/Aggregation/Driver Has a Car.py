class Car:
    def __init__(self,n,no,c):
        self.Cname=n
        self.CNumber=no
        self.Ccolour=c

    def car_start(self):
        print(f"{self.Cname} is started")
    def car_accelerated(self):
        print(f"{self.Cname} is Accelerated")
    def car_stoped(self):
        print(f"{self.Cname} is stoped")



class Driver:
    def __init__(self,n,i,e):
        self.Dname=n
        self.Did=i
        self.Dexperience=e
        n=input("Enter your Car name")
        no=input("Enter your car number")
        c=input("Enter your car colour")
        co=Car(n,no,c)
        self.Dcar=co

    def Driving(self):
        print(f"{self.Dname} Has enter the car")
        self.Dcar.car_start()
        self.Dcar.car_accelerated()
        self.Dcar.car_stoped()
        print(f"{self.Dname} Has came out  the car")



charan=Driver("Charan Kumar B",23763,4)
charan.Driving()
