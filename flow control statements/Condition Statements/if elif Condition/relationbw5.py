print('start')
a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
d=int(input('enter d value'))
e=int(input('enter e value'))

if a==b==c==d==e:
    print('all are the same number')
elif a>b and a>c and a>d and a>e:
    print('a is max')

elif b>c and b>d and b>e:
    print('b is max')

elif c>d and c>e:
    print('c is max')
elif d>e:
    print('d is max')
    
else:
    print('e is max')

print('end')    
