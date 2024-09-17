s=input()
ns=''
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIUO':
        ns+=str(ip)
    else:
        ns+=s[ip]
print(ns)        
