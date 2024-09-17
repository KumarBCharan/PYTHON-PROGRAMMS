with open('first1.txt','wb') as fo:
    import pickle
    d={'name':'charan','age':24}
    bo=pickle.dumps(d)
    print(bo)
    fo.write(bo)
