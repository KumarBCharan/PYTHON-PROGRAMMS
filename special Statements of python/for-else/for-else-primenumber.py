num=int(input())
if num>1:
    
    for i in range(2,num//2+1):
        if num%i==0:
            print('n is not a prime number')
            break
    else:
        print('n is a prime number')
else:
    print('n is not a prime number')
