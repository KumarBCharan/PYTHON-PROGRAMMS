#check given num is perfect or not
n=int(input())
ds=0
for i in  range(1, n//2+1):
    if n%i==0:
        ds+=i
print(ds)        
'''if ds==n:
    print('n is perfect number')
else:
    print('Not Perfect')'''


#Execution
'''
1-> Take input from the user
2-> taking divisor sum =0 assuming that the given input doesnt have any iput
3-> We are taking range b/w 1 to (n//2+1) because any number is divisible by befor half of
    its value so we have taken n//2 if 6//2=3 it retruns range till 2 but we need till 3 so we added +1
    Now range gets till 3
4-> Takin iput as 5
5-> Iteration starts
    Iteration1: extracts 1 and checks condition True ds becomes 1
    Iteration2: extracts 2 and checks condition False ds remains 1
    Iteration3: extracts 3 and checks condition False ds remains 1
    Iteration4: extracts 4 and checks condition False ds remains 1
6-> checks condition n==ds condition false
7-> oput is Not perfect'''
