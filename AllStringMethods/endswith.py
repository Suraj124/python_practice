#endswith(value, start, end)
#The endswith() method returns True if the string ends with the specified value, otherwise False.
s="Python is Awesome"
print(s.endswith("Awesome"))   #True

print(s.endswith("AWesome"))   #False

print(s.endswith("is Awesome")) #True

print(s.endswith("Awesome",5)) #after 5th postion

print(s.endswith("Awesome",5,10))   # between 5th and 10th position