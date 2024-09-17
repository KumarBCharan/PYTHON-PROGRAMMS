with open('first1.txt','rb') as fo:
    import pickle
    bo=fo.read()
    #print(bo)
    print(pickle.loads(bo))
    
