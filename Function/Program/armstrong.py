#4.Armstrong Number or not  AND Armstrong numbers in a given range
'''
def isArmstrong(n):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==n:
        return True
    else:
        return False
#print(isArmstrong(371))
def armstrongNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isArmstrong(num):
            print(num)
armstrongNumbers(2,1000)

OUTPUT:

2
3
4
5
6
7
8
9
153
370
371
407
'''
