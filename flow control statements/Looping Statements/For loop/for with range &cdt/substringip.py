s=input()
sub=input()
count=0
for ip in range(len(s)):
    if s[ip:ip+len(sub):]==sub:
        count+=ip
        print(ip,s[ip:ip+len(sub):])
print(count)        
        
