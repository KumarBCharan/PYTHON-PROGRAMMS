#7.Perfect Number or not  AND Perfect numbers in a given range
'''
def isPerfect(n):
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if ds==n:
        return True
    else:
        return False
#print(isPerfect(28))
def perfectNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isPerfect(num):
            print(num)
perfectNumbers(5,1000)

OUTPUT:

6
28
496
'''
