#1.First n number of special numbers
c=int(input())
n=1
sc=0

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
    if sc==c:
        break
    n+=1
