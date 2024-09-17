with open('first.txt','r') as f:
    import json
    jd=f.read()
    print(jd)
    pd=json.loads(jd)
    print(pd)
    
