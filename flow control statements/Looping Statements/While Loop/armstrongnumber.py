n=int(input())
sum=0
fake=n
l=len(str(n))
while fake>0:
    rem=fake%10
    fake=fake//10
    sum+=rem**l
print(sum)
if sum==n:
    print('n is armstrong number')
else:
    print('n is not armstrong number')
    
