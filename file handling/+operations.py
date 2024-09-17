'''
fo=open('first.txt','w+')
fo.write('hello guys')

print(fo.seek(0))
data=fo.read()
print(data)
'''
'''
f=open('first.txt','a+')
print(f.seek(0))
d=f.read()

print(d)
f.write(" i am charan")
print(f.seek(0))
d=f.read()

print(d)
'''
'''
fo=open('vammoo.txt','x+')
fo.write("this is charan kumar B From Andhra Pradhesh")
print(fo.seek(0))
d=fo.read()

print(type(d))
print(d)
'''
fo=open('first.txt','r+')

fo.write(' i am a python developerrrrrrrrr')

d=fo.read()
print(d)
fo.close()
