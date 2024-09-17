#3.Nth to Nth PERfect Numbers

n=1
pc=0
while True:
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    
    if ds==n:
        pc+=1
        if pc>=3 and pc<=4:
            print(n)
    if pc==15:
        break
    n+=1
