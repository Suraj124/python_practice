from datetime import date,time,datetime

d=date(2018,4,12)
t=time(12,30)
dt=datetime.combine(d,t)
print(dt)