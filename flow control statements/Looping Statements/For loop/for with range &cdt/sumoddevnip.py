s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==1:
            if ip%2==0:
                sum+=int(s[ip])
                print(ip,s[ip])
print(sum)                
print(len(s))               
