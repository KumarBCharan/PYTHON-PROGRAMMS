#4.while loop inside another while loop
print('start')
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)  
        j+=1
        
    i+=1
print('end')
#Breaking inner loop with inner loop value
print('start')
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if j==3:
            break
        j+=1
        
    i+=1
print('end')
#Breaking inner loop with outer loop value
print('start')
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j+=1
        
    i+=1
print('end')

#Breaking outer loop with outer loop value(1)
print('start')
i=1
while i<6:
    if i==3:
        break
    j=1
    while j<6:
        print(i,j)
        
        j+=1
        
    i+=1
print('end')
#Breaking outer loop with outer loop value(2)
print('start')
i=1
while i<6:
    
    j=1
    while j<6:
        print(i,j)
        
        j+=1
    if i==3:
        break   
    i+=1
print('end')
#Breaking outer loop with inner loop value
print('start')
i=1
while i<6:
    
    j=1
    while j<6:
        print(i,j)
        
        j+=1
    if j==6:
        break   
    i+=1
print('end')
'''
#Breaking outer loop with inner loop value
print('start')
i=1
while i<6:
    if j==3:
        break
    
    j=1
    while j<6:
        print(i,j)
        
        j+=1
       
    i+=1
print('end')


OUTPUT:name error becoz i defined j in 4th line then i can't use in 2nd line
'''
