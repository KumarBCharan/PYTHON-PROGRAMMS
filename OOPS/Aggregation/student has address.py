class Address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_details(self):
        print(f"city of the student is {self.city}")
        print(f"state of the student is {self.state}")
        print(f"country of the student is {self.country}")
Bangalore=Address("bangalore","karnataka","india")

class Student:
    def __init__(self,n,a,c,ad):
        self.Sname=n
        self.Sage=a
        self.Sclass=c
        self.Saddress=ad
    def student_details(self):

        print(f"name the student is {self.Sname}")
        print(f"age of the student is{self.Sage}")
        print(f"class of the student is {self.Sclass}")
        print(f":address of the student is: ")
        self.Saddress.display_details()
charan=Student("Charan Kumar B",17,12,Bangalore)
charan.student_details()
