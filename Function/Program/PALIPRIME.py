#PALIPRIME NUMBERS IN A GIVEN RANGE
def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
            else:
                return True
#print(isPrime(11))
def reverse(num):
    dummy=num
    rev=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        rev=rev*10+rem
    return rev

def isPaliPrime(i):
    rev=reverse(i)
    if isPrime(i) and i==rev:
        return True
    else:
        return False
#print(isPaliPrime(11))
def paliPrimeNum(ll,ul):
    
    for i in range(ll,ul+1):
        
        if isPaliPrime(i):
             print(i)
paliPrimeNum(2,200)
'''
OUTPUT:
    5
7
9
11
33
55
77
99
101
111
121
131
141
151
161
171
181
191
'''
