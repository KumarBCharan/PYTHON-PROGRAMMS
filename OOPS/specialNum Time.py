def time(args):
    def inner():
        import time
        T1=time.time()
        args()
        T2=time.time()
        print("time",T2-T1)
    return inner
@time
def specialNum():
    sc=0
    n=100
    while True:
        d=n
        summ=0
        while d>0:
            rem=d%10
            d//=10
            fact=1
            
            for i in range(1,rem+1):
                fact*=i
            summ+=fact
        if summ==n:
            print(n)
            sc+=1
        if sc==5:
            break
        n+=1
specialNum()
