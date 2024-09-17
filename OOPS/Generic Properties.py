class Bank:
    bank_name="UBIN"
    bank_ifsc=517424
    bank_roi=5
    bank_address="Bangalore"
charan=Bank()
vishnu=Bank()
#Accessing of Generic Properties By using Class
#syntax:
    #className.ClassVariableName
print(Bank.bank_ifsc)
print(Bank.bank_address)
#Accessing of Generic Properties By using an Object
#syntax:
    #ObjectName.ClassVariableName
print(charan.bank_address)
print(vishnu.bank_address)

#MOdifying of Generic Properties By using  class
#syntax:
    #ClassName.ClassVariableName=NewValue

Bank.bank_roi=3
print(Bank.bank_roi)
print(charan.bank_roi)
print(vishnu.bank_roi)
#note:
''' if u modify generic properties by using class it will modify in class and as well as in objects'''
#MOdifying of Generic Properties By using an Object
#syntax:
    #objectName.ClassVariableName=NewValue
charan.bank_address="Mysore"
print(charan.bank_address)
print(Bank.bank_address)
print(vishnu.bank_address)
#Note:
''' if u modify generic properties by using an object it will modify in  only that object'''


#Creating New Generic Properties By using class
#Syntax:
        #classNAme.NewClassVAriableName=value
Bank.bank_helpLine="9346096771"
print(Bank.bank_helpLine)
print(charan.bank_helpLine)
print(vishnu.bank_helpLine)

