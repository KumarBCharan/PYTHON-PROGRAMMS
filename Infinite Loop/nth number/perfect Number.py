#2.Nth Perfect number
c=int(input())
n=1
pc=0
while True:
    
    sd=0
    for i in range(1,n//2+1):
        if n%i==0:
            sd+=i
    if n==sd:
        
        pc+=1
    if c==pc:
        print(n)
        break
    n+=1
