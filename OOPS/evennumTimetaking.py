def time(args):
    def inner():
        import time
        Time1=time.time()
        args()
        Time2=time.time()
        print("Time taken for print the values",Time2-Time1)
    return inner
@time
def evenNum():
    c=0
    n=1
    while True:
        if n%2==0:
            print(n)
            c+=1
        if c==10:
            break
        n+=1

evenNum()
