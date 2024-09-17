print("starts")
l=[11,22,33,44,55,66]
ip=int(input("enter which one we need"))
try:
    print("try is started")
    ele=l[ip-1]
    print(ele)
    div=int(input("enter divisor"))
    res=ele/div
    print("try is ended")
except Exception as e:
    print(e)
else:
    print(res)
    
print("ends")
