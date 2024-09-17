def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
#print(isPrime(25))

def phone(num):
    d=num
    summ=0
    while d>0:
        rem=d%10
        d//=10
        if isPrime(rem):
            
            summ+=rem
    print(summ)
    if isPrime(summ):
        return True
    else:
        return False
    
  
print(phone(6304824343))
                
