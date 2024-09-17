#1.Firstn number of disarium Numbers
c=int(input())
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
        print(n)
        dc+=1
    if c==dc:
        break
    n+=1
