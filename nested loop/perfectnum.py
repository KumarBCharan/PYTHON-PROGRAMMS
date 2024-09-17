#WAP to print perfect numbers in a given range
ll=int(input())
ul=int(input())
#Here for loop inside another for loop
print('start')
for num in range(ll,ul+1):
    ds=0
    for i in range(1,num//2+1):
        if num%i==0:
            ds+=i
    if ds==num:
        print(num)
        
print('end')
#Here while loop inside another for loop
print('start')
for num in range(ll,ul+1):
    ds=0
    i=1
    while i<num//2+1:
        if num%i==0:
            ds+=i
        i+=1
    if ds==num:
        print(num)
print('end')
#Here while loop inside another while loop
print('start') 
num=ll
while num<ul+1:
    
    ds=0
    i=1
    while i<num//2+1:
        
        if num%i==0:
            
            ds+=i
            
        i+=1
    if ds==num:
          
        print(num)
        
    num+=1
print('end')
#Here for loop inside another while loop
print('start')
num=ll
while num<ul+1:
    
    ds=0
    for i in range(1,num//2+1):
        
        if num%i==0:
            
            ds+=i
 
    if ds==num:
        print(num)
    
    num+=1


print('end')
