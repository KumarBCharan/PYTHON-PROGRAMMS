with open('vammmmo.txt','xb') as fo:
    import pickle
    d={'name':'cherry','age':25,"mobile":9346097618}
    f=pickle.dump(d,fo)
    
