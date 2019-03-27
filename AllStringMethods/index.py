#The index() method returns the index of a substring inside the string (if found).
#  If the substring is not found, it raises an exception.
#index(value, start, end)

st='Have nice day !. Good day'
print(st.index("day"))

print(st.index("day",11))

# print(st.index("day"11,15))  #will give an error if substring is not found