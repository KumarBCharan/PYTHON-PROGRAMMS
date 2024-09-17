#3.Nth to Nth Armstrong Numbers

n=1
ac=0
while True:
    d=n
    summ=0
    l=len(str(d))
    while d>0:
        rem=d%10
        d//=10
        summ+=rem**l
    if summ==n:
        ac+=1
        if ac>=6 and ac<=15:
            print(n)
    if ac==15:
        break
    n+=1
