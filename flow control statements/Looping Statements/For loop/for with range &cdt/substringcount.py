s=input()
sub=input()
count=0
for ip in range(len(s)):
    if s[ip:ip+len(sub):]==sub:
        count+=1
        print(ip,s[ip:ip+len(sub):])
print(count)        
        
