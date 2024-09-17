'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==n or col==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

'''
    
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==n or col==1:
            print('*',end=' ')
        elif row%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if ((row+col==n-1 and row<=n//2) or (row==col and row<=n//2)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#normal tri
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#reverse tri

n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
