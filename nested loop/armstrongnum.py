ll=int(input())
ul=int(input())
for num in range(ll,ul+1):
    dummy=num
    summ=0
    l=len(str(num))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==num:
        print(num)
