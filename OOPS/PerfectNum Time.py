def time(args):
    def inner():
        import time
        T1=time.time()
        args()
        T2=time.time()
        print("Time Taken",T2-T1)
    return inner
@time
def perfectNum():
    pc=0
    n=1
    
    while True:
        ds=0
        for i in range(1,n//2+1):
            if n%i==0:
                ds+=i
        if ds==n:
            print(n)
            pc+=1
        if pc==4:
            break
        n+=1
        
perfectNum()
