s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==0:
            if ip%2==1:
                sum+=int(s[ip])
                print(ip,s[ip])

print(sum)                
                
