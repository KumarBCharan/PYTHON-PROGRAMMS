#1.First n number of armstrong numbers

c=int(input())
num=1
ac=0

while True:
    d=num
    summ=0
    l=len(str(d))
    
    while d>0:
        rem=d%10
        d//=10
        summ+=rem**l
    if summ==num:
        print(num)
        ac+=1
    
    if c==ac:
        break
    num+=1
