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

    Mycar=Car("THAR","KA53B7418","Black")

    class Driver:
        def __init__(self,n,i,e,dc):
            self.Dname=n
            self.Did=i
            self.Dexperience=e
            self.Dcar=dc

        def Driving(self):
            print(f"{self.Dname} Has enter the car")
            self.Dcar.car_start()
            self.Dcar.car_accelerated()
            self.Dcar.car_stoped()
            print(f"{self.Dname} Has came out  the car")



    charan=Driver("Charan Kumar B",23763,4,Mycar)
    charan.Driving()
