n=int(input())
sum=0
fake=n
while fake>0:
    rem=fake%10
    fake=fake//10
    sum+=rem
print(sum)
if n%sum==0:
    print('n is harshad number')
else:
    print('n is not harshad number')
