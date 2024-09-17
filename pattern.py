
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
'''


def isEmail(s):
    import re
    mpo=re.findall('[a-zA-Z1-9]\w*[.]?\w+@gmail[.]com',s)
    for i in mpo:
        print(i)

    
print(isEmail("kumar@gmail.comjhgf76 asifaharshad@gmail.com 272jyababa.hjc@gmail.com #baba&hjc@gmail.com"
))



'''








