l=eval(input())
ec=0
oc=0

for i in l:
    if isinstance(i,int) and i%2==0:
        
        ec+=i
    else:
        oc+=i


print(ec)
print(oc)
print(abs(oc-ec))
