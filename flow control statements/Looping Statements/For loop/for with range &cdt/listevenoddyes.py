l=eval(input())
for ip in range(len(l)):
    if l[ip]%2==0:
        l[ip]='even'

    else:
         l[ip]='odd'

print(l)    
