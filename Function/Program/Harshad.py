#6.Harshad Number or not  AND Harshad numbers in a given range
'''
def isHarshad(n):
    d=n
    summ=0
    while d>0:
        rem=d%10
        d//=10
        summ+=rem
    if n%summ==0:
        return True
    else:
        return False
#print(isHarshad(30))
def harshadNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isHarshad(num):
            print(num)
harshadNumbers(13,60)

OUTPUT:

18
20
21
24
27
30
36
40
42
45
48
50
54
60
'''
