
def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
            
        else:
            return True
    else:
        return False
#print(isPrime(19))
def reverse(num):
    d=num
    r=0
    while d>0:
        rem=d%10
        d//=10
        r=r*10+rem
    return r
def isEmirp(i):
    rev=reverse(i)
    if i!=rev and isPrime(i) and isPrime(rev):
        return True
#print(isEmirp(113))
def emirpNum(count):
    c=0
    n=1
    while True:
        
        if isEmirp(n):
            print(n)
            c+=1
        if c==count:
                break
        n+=1
emirpNum(10)
