'''#2.For loop inside another while loop
print('start')
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    i+=1
    
print('end')
#Breaking inner loop with inner loop value
print('start')
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
    i+=1
    
print('end')
#Breaking inner loop with outer loop value
print('start')
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if i==3:
            break
    i+=1
    
print('end')
#Breaking outer loop with outer loop value(1)
print('start')
i=1
while i<6:
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
        
    i+=1
    
print('end')
#Breaking outer loop with outer loop value(2)
print('start')
i=1
while i<6:
    
    for j in range(1,6):
        print(i,j)

    if i==3:
        break
    i+=1
    
print('end')
#Breaking outer loop with inner loop value
print('start')
i=1
while i<6:
    
    for j in range(1,6):
        print(i,j)

    if j==5:
        break
    i+=1
    
print('end')
'''
#Breaking outer loop with outer loop value
print('start')
i=1
while i<6:
    if j==3:
        break
    
    for j in range(1,6):
        print(i,j)

    
    i+=1
    
print('end')
