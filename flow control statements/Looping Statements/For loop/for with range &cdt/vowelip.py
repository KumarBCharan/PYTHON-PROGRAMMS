s=input()
v='aeiuoAEIUO'
for ip in range(len(s)):
    if s[ip].isalpha():
        if s[ip] in v:
            print(ip,s[ip])
    
