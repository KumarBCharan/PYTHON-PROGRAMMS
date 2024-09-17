#3.while loop inside another for loop
print('start')

for i in range(1,4):
    j=1
    while j<4:
        print(i+j)
        j+=1
print('end')
#Breaking inner loop with inner loop value
print('start')
for i in range(1,4):
    j=1
    while j<4:
        print(i,j)
        if j==2:
            break
        j+=1
print('end')
#Breaking inner loop with outer loop value
print('start')
for i in range(1,4):
    j=1
    while j<4:
        print(i,j)
        if i==3:
            break
        j+=1
print('end')
#Breaking outer loop with outer loop value
print('start')
for i in range(1,4):
    if i==2:
        break
    j=1
    while j<4:
        print(i,j)
        
        j+=1
print('end')
#Breaking outer loop with outer loop value
print('start')
for i in range(1,4):
    
    j=1
    while j<4:
        print(i,j)
        
        j+=1
    if i==2:
        break
print('end')
#Breaking outer loop with inner loop value
print('start')
for i in range(1,4):
    
    j=1
    while j<4:
        print(i,j)
        
        j+=1
    if j==4:
        break
print('end')
