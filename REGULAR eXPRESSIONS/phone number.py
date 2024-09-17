def regular():
    import re
    data="['hello','harshad','+11-76543','+91-8978239767','+91-9346096771','821729772','+91-9886885132']"
    obj=re.findall('[+]91-[6-9][0-9]{9}',data)
    print(obj)
    
    for i in obj:
        print(i)
    
    
    
regular()
