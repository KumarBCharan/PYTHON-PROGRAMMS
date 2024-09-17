#Emirp Number or nOt AND emirp numebrs in a given range


def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
#print(isPrime(37))

def reverse(num):
    rev=0
    dummy=num
    while dummy>0:
        rem=dummy%10
        dummy//=10
        rev=rev*10+rem
    return rev

def isEmirp(i):
    rev=reverse(i)
    if isPrime(i) and i!=rev and isPrime(rev):
        return True
    else:
        return False
def emirpNum(ll,ul):
    for i in range(ll,ul+1):
        if isEmirp(i):
            print(i)
emirpNum(2,1000)

'''
OUTPUT:
   13
17
31
37
71
73
79
97
107
113
149
157
167
179
199
311
337
347
359
389
701
709
733
739
743
751
761
769
907
937
941
953
967
971
983
991
'''
