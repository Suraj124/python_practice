#The isprintable() methods returns True if all characters in the string are printable or the string
#  is empty. If not, it returns False.
#Characters that occupies printing space on the screen are known as printable characters. For example:
#letters and symbols
#digits
#punctuation
#whitespace
#Example of none printable character can be carriage return and line feed.

st="python 12345"
print(st.isprintable())

st="@#$%^&*"
print(st.isprintable())

st="\n"
print(st.isprintable())

st="\t"
print(st.isprintable())