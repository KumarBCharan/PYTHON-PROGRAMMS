print('start')
s=input()
v='aeiouAIEUO'
c=0

for i in s:
    if i in v:
        c+=1

print(c)
print('end')
