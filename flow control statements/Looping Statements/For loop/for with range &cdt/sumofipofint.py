s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        sum+=ip
        print(ip,s[ip])

print(sum)




