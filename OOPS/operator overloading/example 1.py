class Book:
    def __init__(self,n,a,p):
        print("is created")
        self.Bname=n
        self.Bauthor=a
        self.Bprice=p

    def __str__(self):
        return self.Bname
    def __add__(self,other):
        return self.Bprice+other.Bprice
    
    def __sub__(self,other):
        return self.Bprice-other.Bprice
    def __mul__(self,value):
        return self.Bprice*value
    def __truediv__(self,other):
        return self.Bprice//other

python=Book("Python programming","rossuim",2500)
django=Book("djano laguage","willisom",5000)

#print(python)
#print(python+django)
print(python-django)
print(django-python)
print(django*25)
print(django/2)
