#count(substring, start=..., end=...)
#count() method searches the substring in the given string and returns how many 
#times the substring is present in it.

st="Python is awesome. is not it ?"
print(st.count("is"))

print(st.count("is",9)) #after 9th position 

print(st.count("is",9,12)) # between 9th and 12th position 