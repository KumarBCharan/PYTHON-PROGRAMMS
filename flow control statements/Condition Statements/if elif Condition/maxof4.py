print('start')
a=int(input())
b=int(input())
c=int(input())
d=int(input())

if  a>b and a>c and a>d:
    print('a is max')

elif b>c and b>d:
    print('b is max')

elif c>d:
    print('c is max')
else:
    print('d is max')

print('end')    
