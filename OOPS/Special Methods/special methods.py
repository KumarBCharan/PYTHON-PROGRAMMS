class Book:
    def __init__(self,n,a,p):
        self.Bname=n
        self.Bauthor=a
        self.Bprice=p
        print("object is created so interpreter has called me")

    def __str__(self):
        print("object is printed so interpreter is called me")
        return self.Bname
    def __del__(self):
        print("object is deleted so interpreter has called me")

java=Book("java Programming","Charan kumar",250)
python=Book("python programming an Opps","van guido rossum",2500)
print(java)#print(java.__str__())
#del java
python="cherry"
