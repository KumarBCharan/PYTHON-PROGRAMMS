print("starts")
l=[11,22,33,44,55,66,77,88]
ip=int(input("Enter which element u need"))
try:
    print("try is started")
    ele=l[ip-1]
    print(ele)
    divisor=int(input("enter ur divisor"))
    res=ele/divisor
    print("try is ended")
except:
    print("i am from default block")
else:
    print(res)
print("ends")
