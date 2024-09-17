with open('first.txt','w') as fo:
    import json
    po={'name':'charan','age':21,'mobile':9346096771,'male':True,'female':False,'GF':None}
    print(po)
    jo=json.dumps(po)
    print(jo)
    fo.write(jo)
    
