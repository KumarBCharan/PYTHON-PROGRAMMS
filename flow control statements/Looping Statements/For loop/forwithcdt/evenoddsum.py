print('start')
s=input()
ec=0
oc=0

for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ec+=k
        else:
            oc+=k


print(ec)
print(oc)
print(abs(ec-oc))
