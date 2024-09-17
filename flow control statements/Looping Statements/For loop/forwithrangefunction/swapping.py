l=[11,22,33,44,55,66]
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]

print(l)    
