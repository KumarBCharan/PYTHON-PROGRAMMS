l=eval(input())
for i in range(len(l)):
    if i%2==0:
        

        l[i],l[i+1]=l[i+1],l[i]

print(l)    

