print('start')
s=input()
c=0

for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            c+=k
print(c)
print('end')
        
