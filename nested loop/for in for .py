#1.for loop inside another for loop
print('start')
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
print('end')
#Breaking inner loop with inner loop value
print('start')
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
print('end')   
#Breaking inner loop with outer loop value
print('start')
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if i==3:
            break
print('end')
#Breaking outer loop with outer loop value(1)
print('start')
for i in range(1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
        
print('end')
#Breaking outer loop with outer loop value(2)
print('start')
for i in range(1,6):
   
    for j in range(1,6):
        print(i,j)
    if i==3:
        break   
print('end')

#Breaking outer loop with inner loop value(1)
print('start')
for i in range(1,6):
   
    for j in range(1,6):
        print(i,j)
    if j==5:
        break   
print('end')

'''
#Breaking outer loop with outer loop value(1)
print('start start')
for i in range(1,6):
    if j==3:
        break
    for j in range(1,6):
        print(i,j)
        
print('end')
REsult::NAme error becoz i used in 2 lind but,i defined this variable in 4 line
'''
