n=int(input())
ds=0
i=1
while i<n//2+1:
    if n%i==0:
        ds+=i
        print(i)
    i+=1
if ds==n:
    print('perfect')
else:
    print('not perfect')
