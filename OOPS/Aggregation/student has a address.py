class Address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_details(self):
        print(f"city of the student is {self.city}")
        print(f"state of the student is {self.state}")
        print(f"country of the student is {self.country}")


class Student:
    def __init__(self,n,a,c):
        self.Sname=n
        self.Sage=a
        self.Sclass=c
        c=input("enter city name")
        s=input("enter state name")
        co=input("enter country name")
        aco=Address(c,s,co)
        self.Saddress=aco
    def student_details(self):

        print(f"name the student is {self.Sname}")
        print(f"age of the student is{self.Sage}")
        print(f"class of the student is {self.Sclass}")
        print(f":address of the student is  ")
        self.Saddress.display_details()
charan=Student("Charan Kumar B",17,12)
charan.student_details()
