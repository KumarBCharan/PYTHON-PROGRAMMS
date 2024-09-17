def divide_without_error(args):
    def inner(a,b):
        if b!=0:
            args(a,b)
        else:
            args(b,a)
    return inner
@divide_without_error
def division(a,b):
    print(a/b)
division(10,0)
    
    
