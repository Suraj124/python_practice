#The partition() method splits the string at the first occurrence of the argument string 
# and returns a tuple containing the part the before separator, argument string and
#  the part after the separator.

st="Python is awesome"
t=st.partition("is")
print(t)

st="Python is awesome python is awesome"
t=st.partition("python ")
print(t)