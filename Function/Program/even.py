#2.Even NUmber and Even numbers in a given range
'''
def isEven(n):
    if n%2==0:
        return True
    else:
        return False

#print(isEven(8))
def evenNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isEven(num):
            print(num)
evenNumbers(2,25)
'''
