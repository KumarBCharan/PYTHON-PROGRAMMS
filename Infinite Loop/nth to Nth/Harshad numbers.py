#3.Nth to Nth Harshad Numbers

n=1
hc=0
while True:
    d=n
    summ=0
    while d>0:
        rem=d%10
        d//=10
        summ+=rem
    if n%summ==0:
        hc+=1
        if hc>=8 and hc<=22:
            print(n)
    if hc==22:
        break
    n+=1
