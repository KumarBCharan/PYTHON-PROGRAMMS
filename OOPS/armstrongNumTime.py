def time(args):
    def inner():
        import time
        T1=time.time()
        args()
        T2=time.time()
        print("Time Taking",T2-T1)
    return inner
@time
def armstrongNum():
    ac=0
    n=100
    while True:
        d=n
        summ=0
        l=len(str(n))
        while d>0:
            rem=d%10
            d//=10
            summ+=rem**l
        if summ==n:
            print(n)
            ac+=1
        if ac==10:
            break
        n+=1
armstrongNum()
