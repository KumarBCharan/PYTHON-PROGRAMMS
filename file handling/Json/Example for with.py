with open('new.txt','w+') as fo:
    fo.write("Hai AAfiya Thabasum")
    fo.seek(0)
    d=fo.read()
    print(d)
    
    print(fo.closed)
print(fo.closed)
             
