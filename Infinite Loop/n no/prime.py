#1.First n number of Prime numbers
c=int(input())
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
    if c==pc:
        break
    n+=1
