#1.First n number of Perfect Numbers
c=int(input())
n=1
pc=0
while True:
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if ds==n:
        print(n)
        pc+=1
    if c==pc:
        break
    n+=1
