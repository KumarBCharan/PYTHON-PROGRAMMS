a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a>b:
    if a>c:
        if a>d:
            print('a is max')
        else:
            print('d is max')
    else:
        if c>d:
            print('c is max')
        else:
            print('d is max')

else:
    if b>c:
        if b>d:
            print('b is max')
        else:
            print('d is max')

    else:
        if c>d:
            print('c is max')
        else:
            print(' d is max')
            
            
