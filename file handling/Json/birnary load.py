with open('first1.txt','rb') as fo:
    import pickle
    po=pickle.load(fo)
    print(po)
