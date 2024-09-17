print("starts")
l=[11,22,33,44,55,66]
ip=int(input("enter which element we need"))
try:
    print("try is started")
    ele=l[ip-1]
    print(ele)
    divisor=int(input("enter your divisor"))
    #print(divisor)
    res=ele/divisor
    print("try is ended")
except IndexError as ie:
    print(ie)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(res)
    
print("ends")
