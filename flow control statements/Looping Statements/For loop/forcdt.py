#for loop with String
s='Charan Kumar'

for i in s:
    print(i)
   
#for loop with List
l=[11,22,33,'cherry',88]

for k in l:
    print(k)
    print('list')
     
#for loop with tuple
t=(11,22,(33,44),[55,'hello'],879)

for k in t:
    print(k)

#for loop with set
s={11,22,(33,44),55,'hello',879}

for k in t:
    print(k)

#for loop with dictionary
d={11:22,'name':'cherry',55:'hello'}

for k in d:
    print(k,d[k])

#for loop with dictionaries items method
#(we need to use two variables as data in dictionaries we have in the form of key and value pairs)
d={'gfname':'Ammu','bfname':'cherry','amma':'prema','nanna':'venu','akka':'lakshmi','mama':'mahesh'}
for p,v in d.items():
    print(p,v)
