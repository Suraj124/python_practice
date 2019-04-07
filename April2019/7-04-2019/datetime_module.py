from datetime import time,date

t=time(4,20,45)

print(t)

print('Hour=',t.hour)
print('Minute=',t.minute)
print('Seconds=',t.second)
print('Microsecond=',t.microsecond)
print('Time zone information=',t.tzinfo)

#----------------------------------------------#

#We can also check the min and max values a time of day can have in the module:

print(time.min)
print(time.max)

#-----------------------------------------------------#

## Date ##

d=date.today()
print(d)

print('Year=',d.year)
print('Month=',d.month)
print('Day=',d.day)
print(d.ctime())

#--------------------------------------------------------#

#As with time, the range of date values supported can be determined using the min and max attributes.

print(d.min)
print(d.max)

#-----------------------------------------------------------#

d1=date(2019,4,12)
print(d1)
print(d1.day)

#replace year month day

d2=d1.replace(year=2020)

print(d2)

#-----------------------------------------#

print(d2-d1)