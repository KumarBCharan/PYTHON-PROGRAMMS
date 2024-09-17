s=input()
v='aeiouAEIUO'
ns=''
i=0
while i<len(s):
    if s[i] in v:
        ns+=str(i)
    else:
        ns+=s[i]
    i+=1
print(ns)

#Execution of reverse String

'''
1->Taking  String input from the user .(power star)
2->now take a another empty string ns .
2->Create v with 'aeiouAEIUO' as value.
3->Extraction Starts
    Iteration1: Extract 'p' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration2: Extract 'o' checks r in a or not,it is True ,then replace with it's ip value and  add into ns the ns becomes 'p1'
    Iteration3: Extract 'w' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration4: Extract 'e' checks r in a or not,it is True ,then replace with it's ip value and  add into ns the ns becomes 'p1w3'
    Iteration5: Extract 'r' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration6: Extract ' ' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration7: Extract 's' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration8: Extract 't' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration9: Extract 'a' checks r in a or not,it is True ,then replace with it's ip value and  add into ns the ns becomes 'p1w3r st'
    Iteration3: Extract 'p' and add into rev Then rev becomes 'rats rewop'
    
4->Now print the rev as rats rewop.
'''

