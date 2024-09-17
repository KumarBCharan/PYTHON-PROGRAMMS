class Employee:
    company_name="Infosys"
    company_address="Bangalore"
    company_empCount=0

    def __init__(self,n,i,s):
        empname=n
        empid=i
        empsalary=s

        Employee.company_empCount+=1
    def __del__(self):
    
        Employee.company_empCount-=1

charan=Employee("Charan Kumar B",25489,27000)
mahesh=Employee("Mahesh Kumar V",25499,35000)
print(charan.company_empCount)
print(mahesh.company_empCount)
print(Employee.company_empCount)
del charan
print("chara was resinged for the company")
print(mahesh.company_empCount)
print(Employee.company_empCount)

