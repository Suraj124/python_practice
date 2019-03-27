#The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
#string.isdigit()

st="1234"
print(st.isdigit())

st="1234 5678"
print(st.isdigit())

st="12zx"
print(st.isdigit())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())