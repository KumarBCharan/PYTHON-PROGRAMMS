with open('new.txt','w') as fo:
    import json
    po={'name':'charan','age':21,'mobile':9346096771,'male':True,'female':False,'GF':None}
    print(po)
    jo=json.dump(po,fo)
    print(jo)
