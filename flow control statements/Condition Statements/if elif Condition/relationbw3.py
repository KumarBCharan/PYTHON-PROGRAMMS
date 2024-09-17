print('start')
csk=int(input('Enter a value'))
mi=int(input('Enter b value'))
rcb=int(input('Enter c value'))

if csk==mi==rcb:
    print('share the price money')
elif csk>mi and csk>rcb:
    print('csk is the winner')

elif mi>rcb:
    print('mi is the winner')

else:
    print('rcb is the winner')


print('end')    
