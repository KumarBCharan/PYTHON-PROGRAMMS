s="hai123bye55bri2cherry43h7"
summ=0
import re
obj=re.findall('\d+',s)
for i in obj:
    
    if int(i)%2==1:
        print(i)
        summ+=int(i)
print(summ)
