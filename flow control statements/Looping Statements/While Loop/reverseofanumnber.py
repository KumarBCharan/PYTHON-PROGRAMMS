n=int(input())
rev=0
fake=n
while fake>0:
    rem=fake%10
    fake=fake//10
    rev=rev*10+rem
print(rev)
