print('start')
word1=input('Enter a value:')
word2=input('Enter b value:')
a=sorted(word1,reverse=True)
b=sorted(word2,reverse=True)
print(a)
print(b)


if a==b:
    print('both are anagrams')

else:
    print('Both are not anagrams')


print('end')    

'''a='calm'
b='clam'
aa=sorted(a,reverse=True)
bb=sorted(b,reverse=True)
print(aa)
print(bb)
if aa==bb:
    print('is correct')

else:
    print('is wrong')'''
    
