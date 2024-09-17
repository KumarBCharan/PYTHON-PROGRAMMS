class A:
    house="2BHK"
    bike="chetak"
class B(A):
    bike="Royal Enfield"
    money="250000"
OA=A()
OB=B
#Modifying Parent class properties by using parent class
A.house="4BHK"
print(A.house)
print(B.house)
print(OA.house)
print(OB.house)
print("\n")  
#NOte:
'''
IF we modify parent class properties by using parent class it will modify
parent class ,child class and thier objetcs
'''
#Modifying Parent class properties by using parent class Object
OA.house="4BHK"
print(A.house)
print(B.house)
print(OA.house)
print(OB.house)
print("\n")
#NOte:
'''
If we modify Parent class properties by using parent class Object it will modify/affect on only that
particular object  it will not affect on other.
'''
#Modifying Parent class properties by using child class 
B.house="4BHK"
print(A.house)
print(B.house)
print(OA.house)
print(OB.house)
print("\n")

#NOte:
'''
IF we modify parent class properties by using child class it will modify
child class  and its objetcs
'''

#Modifying Parent class properties by using child class object
OB.house="4BHK"
print(A.house)
print(B.house)
print(OA.house)
print(OB.house)
print("\n")

#NOte:
'''
IF we modify parent class properties by using child class object it will modify/affect on only that
particular object  it will not affect on other.
'''
