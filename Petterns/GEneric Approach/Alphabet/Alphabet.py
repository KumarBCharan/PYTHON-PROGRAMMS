
#1.Example
'''
n=int(input())
star=1

for row in range(1,n+1):
    dummy=65
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
    star+=1


OUTPUT:

 5
A 
A B 
A B C 
A B C D 
A B C D E 
'''

#2.Example
'''
n=int(input())
dummy=65
for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(dummy),end=' ')
    print()
    dummy+=1


OUTPUT:
    5
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
'''

#3.Example
'''
n=int(input())
dummy=65
for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
    
    
OUTPUT:
    5
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
'''
#4.Example
'''
n=int(input())
for row in range(1,n+1):
    dummy=65
    for col in range(1,n+1):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
    
OUTPUT:
    5
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E
'''

#5.Example
'''
n=int(input())
star=1
dummy=65
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        
    print()
    star+=1
    dummy+=1

OUTPUT:
    5
A 
B B 
C C C 
D D D D 
E E E E E 
'''
#6.Example
    
'''
n=int(input())
star=1
dummy=65
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
    star+=1

OUTPUT:
    5
A 
B C 
D E F 
G H I J 
K L M N O 
'''
#7.Example
''' 
n=int(input())

for row in range(1,n+1):
    dummy=row+64
    for col in range(1,n+1):
        print(chr(dummy),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
 
OUTPUT:

5
A B C D E 
B D F H J 
C D E F G 
D F H J L 
E F G H I 
'''
#8.Example
'''
n=int(input())
for row in range(1,n+1):
    dummy=row+64
    
    for st in range(1,n+1):
        print(chr(dummy),end=' ')
        dummy+=row
    print()
    
  
OUTPUT:

5
A B C D E 
B D F H J 
C F I L O 
D H L P T 
E J O T Y 
'''
#9.Example
'''
n=int(input())
star=n
dummy=65
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        if row%2==1:
            
            dummy+=1
        else:
            dummy-=1
    print()
    star-=1

OUPUT:

5
A B C D E 
F E D C 
B C D 
E D 
C
'''
#10.Example
'''
n=int(input())
star=1
space=n-1
for row in range(1,n+1):
    dummy=65
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
    star+=2
    space-=1

OUTPUT:

5
        A 
      A B C 
    A B C D E 
  A B C D E F G 
A B C D E F G H I

'''
#11.Example
'''
n=int(input())
star=1

for row in range(1,n+1):
    dummy=row+64
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
       
        dummy-=1
    print()
    star+=1


OUTPUT:

5
A 
B A 
C B A 
D C B A 
E D C B A
'''
#12.Example
'''
n=int(input())
star=1
space=n-1

for row in range(1,n+1):
    dummy=65
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        if st<=star//2:
            dummy+=1
        else:
            dummy-=1
            
    print()
    star+=2
    space-=1

OUTPUT:

5
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A
'''
#13.Example
'''
n=int(input())
star=1
space=n//2
for row in range(1,n+1):
    dummy=65
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
        if st<=star//2:
            dummy+=1
        else:
            dummy-=1
    print()
    if row<=n//2:
        star+=2
        
        space-=1
    else:
        star-=2
       
        space+=1
        
   
OUTPUT:

9
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 
  A B C D C B A 
    A B C B A 
      A B A 
        A 

'''
#14.Example
'''
n=int(input())
for row in range(1,n+1):
    dummy=row+64
    for col in range(1,n+1):
        print(chr(dummy),end=' ')
        dummy+=n
    print()

OUTPUT:

5
A F K P U 
B G L Q V 
C H M R W 
D I N S X 
E J O T Y 
'''
#15.Example
'''
n=int(input())
star=1
space=0
dummy=65
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy),end=' ')
    print()
    if row<=n//2:
        dummy+=2
        space+=1
    elif row==n//2+1:
        dummy-=1
        space-=1
        
    else:
        dummy-=2
        space-=1


OUTPUT:

9
A 
  C 
    E 
      G 
        I 
      H 
    F 
  D 
B 

'''
