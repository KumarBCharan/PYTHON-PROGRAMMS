'''
n=int(input())
star=n
space=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
        
    for sp in range(1,star+1):
        print('@',end=' ')
    print()
    if row<=n//2:
        
        space+=1
        star-=2 
    else:
          
        space-=1
        star+=2


'''



n=int(input())
star=1
space=n//2
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
        
    for sp in range(1,star+1):
        print('@',end=' ')
    print()
    if row<=n//2:
        space-=1
        star+=2
        
    else:
        space+=1
        star-=2 
       
