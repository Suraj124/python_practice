from datetime import date
import time
ldates=[]
d1=date(2018,5,22)
d2=date(2017,5,2)
d3=date(2016,4,30)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
 
ldates.sort()

time.sleep(3) # program will wait here for 3 seconds

for i in ldates:
    print(i)