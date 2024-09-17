class Book:
    def __init__(self,n,a,p):
        print("is created")
        self.Bname=n
        self.Bauthor=a
        self.Bprice=p

    def __str__(self):
        return self.Bname
    def __del__(self):

        print("is gone")

charan=Book("charan life story","cherry B",250)
print(charan)
del charan
