#The isalnum() method returns True if all characters in the string are alphanumeric
#  (either alphabets or numbers). If not, it returns False.
#string.isalnum()

st="sam124"
print(st.isalnum())     #True

strr="python"
print(strr.isalnum())       #True

n="123"
print(n.isalnum())      #True

s="hello 123"
print(s.isalnum())  # whitespace is not alphanumeric that is it return False