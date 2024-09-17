n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i


if n==s:
    print('perfect')

else:
    print('not perfect')
