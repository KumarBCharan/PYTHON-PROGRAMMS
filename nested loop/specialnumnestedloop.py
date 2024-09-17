    #WAP to print all the special numbers in a given range 

    ll=int(input())
    ul=int(input())
    for num in range(ll,ul+1):
        dummy=num
        summ=0
        while dummy>0:
            rem=dummy%10
            dummy//=10
            fact=1
            for i in range(1,rem+1):
                fact*=i
            summ+=fact
        if summ==num:
                print(num)

                
    #Explanation Of The program
    1->Taking input from the user as lower limit(ll=145)
    2->Taking input from the user as upper limit(ul=146)
    3->i will fetch the number by for loop from a given range(145,146),
        The first number  fetched as 145 by using num variable
    4->Here i will create  dummy variable with assigning  num value(145) into that for future usage of num.
    5->Create a summ variable by assuming the value as 0(Becoz if the fetched number is 
    6->now i need to check (dummy=145) dummy>0 or not, it is true then controll enter into block
        ITERATION1:
                                                         
        *Then i will find reminder by using rem=dummy%10 i will get 5 as rem
        *now reduce the num by using dummy//=10 i will get num as 14
        *Take fact variable assigning value as 1 (Becoz if the num is 0 the 0 fact is 1)
        *i will fetch the number by for loop from a given range(1,rem+1),
        *The first number  fetched as 1 by using i variable                                              
         I1->now calculate the factorial by using fact*=i now the fact value becomes 1
        *The first number  fetched as 2 by using i variable                                              
         I2->now calculate the factorial by using fact*=i now the fact value becomes 2
         *The first number  fetched as 3  by using i variable                                              
         I3->now calculate the factorial by using fact*=i now the fact value becomes 6
        *The first number  fetched as 4  by using i variable                                              
         I4->now calculate the factorial by using fact*=i now the fact value becomes 24
        *The first number  fetched as 5 by using i variable                                              
         I5->now calculate the factorial by using fact*=i now the fact value becomes 120                                                                                                                                      
        *That fact  add into summ by using summ+=fact summ becomes 120
        ITERATION2:
         now i need to check (dummy=14)  dummy>0 or not, it is true then controll enter into block
        *Then i will find reminder by using rem=dummy%10 i will get 4 as rem
        *now reduce the num by using dummy//=10 i will get num as 1
        *Take fact variable assigning value as 1 (Becoz if the num is 0 the 0 fact is 1)
        *i will fetch the number by for loop from a given range(1,rem+1),
        *The first number  fetched as 1 by using i variable                                              
         I1->now calculate the factorial by using fact*=i now the fact value becomes 1
        *The first number  fetched as 2 by using i variable                                              
         I2->now calculate the factorial by using fact*=i now the fact value becomes 2
         *The first number  fetched as 3  by using i variable                                              
         I3->now calculate the factorial by using fact*=i now the fact value becomes 6
        *The first number  fetched as 4  by using i variable                                              
         I4->now calculate the factorial by using fact*=i now the fact value becomes 24
        *That fact  add into summ by using summ+=fact summ becomes 144
        ITERATION3:
                                                         
        now i need to check (dummy=1)  dummy>0 or not, it is true then controll enter into block
        *Then i will find reminder by using rem=dummy%10 i will get 1 as rem
        *now reduce the num by using dummy//=10 i will get num as 0
        *Take fact variable assigning value as 1 (Becoz if the num is 0 the 0 fact is 1)
        *i will fetch the number by for loop from a given range(1,rem+1),
        *The first number  fetched as 1 by using i variable                                              
         I1->now calculate the factorial by using fact*=i now the fact value becomes 1
        *That fact  add into summ by using summ+=fact summ becomes 145





                                                         
    7->Finally  checks the condition summ==num it is true
        ->Then num will print as 145
                                                         
            
                                           
                                              
                                                         


