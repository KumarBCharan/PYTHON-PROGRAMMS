n=int(input())
dummy=n
sum=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy//=10
    sum+=rem**l
    l-=1
print(sum)
if sum==n:
    print('n is disarium number')
else:
    print('n is not disarium number')
    
