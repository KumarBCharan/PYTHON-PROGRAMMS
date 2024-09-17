print("starts")
l=[11,22,33,44,55,66]
ip=int(input("enter which element u need"))
try:
    print("try is started")
    ele=l[ip-1]
    print(ele)
    divisor=int(input("enter ur divisor"))
    res=ele/divisor
    print("try is ended")
except Exception as e:
    print(e)
else:
    print(res)
finally:
    print("i am from finally block")
print("ends")
