
n=int(input())
star=1
space=n-2
for row in range(1,n+1):
    for st in range(1,star+1):
        print("*",end=' ')
   
    for sp in range(1,space+1):
        print(' ',end='')
    for sp in range(1,space+1):
        print(' ',end='')
    if row==n//2+1 :
        for st in range(1,n+1):
            print("*",end=' ')
    else:
        for st in range(1,star+1):
            print("*",end=' ')
   
        
        
                   
    print()
    if row<=n//2:
        
        star+=1
        space-=2
    else:
        
        star-=1
        space+=2










