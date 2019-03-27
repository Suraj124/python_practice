#The string encode() method returns encoded version of the given string.


s="Python"
print(s.encode())

s2="ön"
print(s2.encode())

print(s2.encode("ascii","ignore"))
print(s2.encode("ascii","replace"))
print(s2.encode("ascii","xmlcharrefreplace"))
print(s2.encode("ascii","namereplace"))
print(s2.encode("utf-8","replace"))