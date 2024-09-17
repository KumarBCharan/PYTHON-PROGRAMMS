def f1():
    print("first line of f1")
    a=10/0
    print("last line of f1")
def f2():
    print("first line of f2")
    try:
         f1()
    except Exception as e:
        print(e)
        
   
    print("last line of f2")
print("main starts")
f2()
print("main ended")
