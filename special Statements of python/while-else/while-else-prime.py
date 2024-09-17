num=int(input())
if num>1:
    
    i=2
    while i<num//2+1:
        
        if num%i==0:
            print('n is not a prime number')
            break
        i+=1
    else:
        print('n is a prime number')
else:
    print('n is not a prime number')
