#1.First n number of Harshad numbers
c=int(input())
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
        print(n)
        hc+=1
    if c==hc:
        break
    n+=1
        
