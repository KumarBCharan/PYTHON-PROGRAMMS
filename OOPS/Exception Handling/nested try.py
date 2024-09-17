print("starts")
try:
    print("outer try is starts")
    #print(a)
    print("hai")
    try:
        print("inner try is ended")
        a=10/0
        print("inner try id ended")
    except Exception as e:
        print(e)
    print("outer try ias ended")
except Exception as e:
        print(e)    
print("ends")
