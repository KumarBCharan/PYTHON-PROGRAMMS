#3.Nth to Nth Special Numbers

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
        sc+=1
        if sc>=2 and sc<=4:
            print(n)
    if sc==4:
        break
    n+=1
