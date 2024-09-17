#2.Nth Disarium number

c=int(input())
n=1
pc=0
while True:
    d=n
    summ=0
    l=len(str(d))
    while d>0:
        rem=d%10
        d=d//10
        summ+=rem**l
        l-=1
    if summ==n:
        
        pc+=1
    if c==pc:
        print(n)
        break
    n+=1
