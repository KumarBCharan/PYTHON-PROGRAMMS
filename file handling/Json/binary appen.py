with open('second.txt','ab') as fo:
    import pickle
    d={'name':'cherry','age':25,"mobile":9346097618}

    bo=pickle.dump(d,fo)
