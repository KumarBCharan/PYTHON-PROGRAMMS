#8.Special Number or not  AND Special numbers in a given range
'''
def isSpecial(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    if summ==n:
        return True
    else:
        return False
#print(isSpecial(145))
def specialNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isSpecial(num):
            print(num)
specialNumbers(2,200)


OUTPUT:
2
145
'''
