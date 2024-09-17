def time(args):
    def inner():
        import time
        T1=time.time()
        
        args()
        T2=time.time()
        
        print("Time Taken",T2-T1)
    return inner
@time
def primeNum():
    pc=0
    n=1
    while True:
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n)
                pc+=1
        if pc==10:
            break
        n+=1
primeNum()
