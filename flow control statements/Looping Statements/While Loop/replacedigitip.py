s=input()

ns=''
i=0
while i<len(s):
    if s[i].isdigit():
        ns+='G'
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
    Iteration1: Extract 'p' checks p is digit or not,it is False. controll will not enter into loop block.
    Iteration2: Extract '1' checks r in a or not,it is True ,then replace with 'G' value and  add into ns the ns becomes 'p1'
    Iteration3: Extract 'w' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration4: Extract '4' checks r in a or not,it is True ,then replace with 'G' value and  add into ns the ns becomes 'p1w3'
    Iteration5: Extract 'r' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration6: Extract ' ' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration7: Extract 's' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration8: Extract 't' checks r in r or not,it is False. controll will not enter into loop block.
    Iteration9: Extract '3' checks r in a or not,it is True ,then replace with 'G' value and  add into ns the ns becomes 'p1w3r st8
    Iteration3: Extract 'r' checks r in r or not,it is False. controll will not enter into loop block.
    
4->Now print the ns as pGwGr stGr.
'''
