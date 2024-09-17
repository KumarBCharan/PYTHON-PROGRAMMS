s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        sum+=int(s[ip])
        print(ip,s[ip])

print(sum)  

'''
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)    '''    
