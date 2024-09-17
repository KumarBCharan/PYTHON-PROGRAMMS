#3.Prime Number or not  AND Prime numbers in a given range
'''
def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
#print(isPrime(37))
def primeNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isPrime(num):
            print(num)
primeNumbers(2,38)


OUTPUT:

2
3
5
7
11
13
17
19
23
29
31
37
'''
