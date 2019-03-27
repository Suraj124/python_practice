from datetime import date
import time

start_Time=time.perf_counter()

ldates=[]
d1=date(2018,5,22)
d2=date(2017,5,2)
d3=date(2016,4,30)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

for i in ldates:
    print(i)

end_Time=time.perf_counter()

print("Time Execution: ",end_Time-start_Time)