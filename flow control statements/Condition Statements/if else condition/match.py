print('start')
mi=int(input("Enter the mi team score:"))
rcb=int(input("Enter the rcb team score:"))

if mi>rcb:
    print('if block')
    print(f'mi score {mi} is greater than rcb score {rcb} then mi won the match')

else:
    print('else block')
    print(f'rcb score {rcb} is greater than mi score {mi} then rcb won the match')

#we can write in another way also

    
if rcb>mi:
    print('if block')
    print(f'rcb score {rcb} is greater than mi score {mi} then rcb won the match')

else:
    print('else block')
    print(f'mi score {mi} is greater than rcb score {rcb} then mi won the match')


print('end')
