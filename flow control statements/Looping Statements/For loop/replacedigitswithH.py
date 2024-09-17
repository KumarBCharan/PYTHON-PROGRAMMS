s=input()
ns=''
'''for ip in range(len(s)):
    if s[ip].isdigit():
        ns+='h'
    else:
        ns+=s[ip]
'''
for ch in s:
    if ch.isdigit():
        ns+='H'
    else:
        ns+=ch
        
print(ns)        














