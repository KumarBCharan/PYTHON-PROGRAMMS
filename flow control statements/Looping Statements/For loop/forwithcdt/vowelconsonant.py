print('start')
s=input()
v='aeiouAIEUO'
vc=0
cc=0

for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1

print(vc)
print(cc)
print('end')
