#WAP to print prime numbers in a given range

ll=int(input())
ul=int(input())
#HERE BY USING For loop inside another for loop
print('start')
for num in range(ll,ul+1):
    
    if num>1:
    
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            print(num)
print('end')
#HERE BY USING For loop inside another while loop
print('start')
num=ll
while num<ul+1:
    if num>1:
        
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            print(num) 
    num+=1
print('end')
#HERE BY USING while loop inside another for loop

for num in range(ll,ul+1):
    if num>1:
        i=2
        while i<num//2+1:
            if num%i==0:
                break
            i+=1
        else:
            print(num)

#HERE BY USING while loop inside another while loop
print('start')
num=ll
while num<ul+1:
    if num>1:
        i=2
        while i<num//2+1:
            if num%i==0:
                break
            i+=1
        else:
            print(num)
    num+=1
    
print('end')
