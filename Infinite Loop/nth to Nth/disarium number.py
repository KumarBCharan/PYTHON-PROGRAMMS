#3.Nth to Nth Disarium Numbers

n=1
dc=0
while True:
    d=n
    summ=0
    l=len(str(d))
    while d>0:
        rem=d%10
        d//=10
        summ+=rem**l
        l-=1
    if summ==n:
        dc+=1
        if dc>=6 and dc<=15:
            print(n)
    if dc==15:
        break
    n+=1
