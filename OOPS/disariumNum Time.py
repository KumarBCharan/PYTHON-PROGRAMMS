def time(args):
    def inner():
        import time
        t1=time.time()
        args()
        t2=time.time()
        print("time taken for printing",t2-t1)
    return inner
@time
def disariumNum():
    dc=0
    n=100
    while True:
        summ=0
        l=len(str(n))
        d=n
        while d>0:
            rem=d%10
            d//=10
            summ+=rem**l
            l-=1
        if summ==n:
            print(n)
            dc+=1
        if dc==8:
            break
        n+=1
disariumNum()
