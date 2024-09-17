#5.Disarium Number or not  AND Disarium numbers in a given range
'''

def isDisarium(n):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
        l-=1
    if summ==n:
        return True
    else:
        return False
#print(isDisarium(175))
def disariumNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isDisarium(num):
            print(num)
disariumNumbers(2,1000)

OUTPUT:

2
3
4
5
6
7
8
9
89
135
175
518
598
'''
