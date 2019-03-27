import re
st="Take up one idea,one idea at a time onion"
print("w+")
result=re.findall(r'o\w+',st)
print(result)

print("w*")
result=re.findall(r'o\w*',st)
print(result)

print("w?")
result=re.findall(r'o\w?',st)
print(result)  # Notice the output of this print()

print("w{m}")
result=re.findall(r'o\w{4}',st)     # after o how many character should be there
print(result)

print("w{m,n}")
result=re.findall(r'o\w{1,4}',st)
print(result)
