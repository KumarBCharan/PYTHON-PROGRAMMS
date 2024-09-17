a=int(input())
b=int(input())
n=int(input())
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b,end=' ')
    for i in range(n-2):
        c=a+b
        print(c,end=' ')
        a,b=b,c
