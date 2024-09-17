'''l=eval(input())
mx=0

for i in l:
    if i>mx:
        mx=i
print(mx)           


l=eval(input())
print(max(l))'''


l=eval(input())
l.sort()
print(l[-1])
    
