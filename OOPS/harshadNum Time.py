def time(args):
    def inner():
        import time
        t1=time.time()
        args()
        t2=time.time()
        print("time guru",t2-t1)
    return inner
@time
def harshadNum():
    hc=0
    n=1
    while True:
        summ=0
        d=n
        while d>0:
            rem=d%10
            d//=10
            summ+=rem
        if n%summ==0:
            print(n)
            hc+=1
        if hc==0:
            break
        n+=1

harshadNum()
