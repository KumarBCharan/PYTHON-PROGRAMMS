s=input()
v='AEIOUaeiuo'
for ip in range(len(s)):
    if s[ip].isalpha() and s[ip] not in v:
        print(ip,s[ip])
        
