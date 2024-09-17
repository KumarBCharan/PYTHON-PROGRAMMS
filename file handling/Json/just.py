with open('new.txt','rb') as fo:
    import pickle
    
    print(pickle.load(fo))
