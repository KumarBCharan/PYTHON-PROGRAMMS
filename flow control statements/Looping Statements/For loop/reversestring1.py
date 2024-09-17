'''s=input()
rev=''
for i in range(-1,-(len(s)+1),-1):
    rev+=s[i]
    print(rev)
print(rev)
'''
s=input()
rev=''
for ch in s:
    rev=ch+rev
print(rev)

#Execution of reverse String

'''
1->Taking  String input from the user .(power star)
2->now take a another empty string rev .
3->Extraction Starts
    Iteration1: Extract 'r' and add into rev Then rev becomes 'r'
    Iteration2: Extract 'a' and add into rev Then rev becomes 'ra'
    Iteration3: Extract 't' and add into rev Then rev becomes 'rat'
    Iteration4: Extract 's' and add into rev Then rev becomes 'rats'
    Iteration5: Extract ' ' and add into rev Then rev becomes 'rats '
    Iteration6: Extract 'r' and add into rev Then rev becomes 'rats r'
    Iteration7: Extract 'e' and add into rev Then rev becomes 'rats re'
    Iteration8: Extract 'w' and add into rev Then rev becomes 'rats rew'
    Iteration9: Extract 'o' and add into rev Then rev becomes 'rats rewo'
    Iteration3: Extract 'p' and add into rev Then rev becomes 'rats rewop'
    
4->Now print the rev as rats rewop.
'''
