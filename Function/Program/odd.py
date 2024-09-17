#1.Odd NUmber and Odd numbers in a given range
'''
def isOdd(n):
    if n%2==1:
        return True
    else:
        return False
#print(isOdd(7))

def oddNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isOdd(num):
            print(num)
oddNumbers(2,25)

OUTPUT:

3
5
7
9
11
13
15
17
19
21
23
25

'''
