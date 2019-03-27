#The isidentifier() method returns True if the string is a valid identifier in Python.
#  If not, it returns False.
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9),
#or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# "Identifier_name".isidentifier()

st="Demo"
print(st.isidentifier())

st="22python"
print(st.isidentifier())

st="sam 1234"
print(st.isidentifier())