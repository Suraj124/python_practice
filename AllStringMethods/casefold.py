#The casefold() method is an aggressive lower() method which convert strings to casefolded strings
# # for caseless matching.The casefold() method is removes all case distinctions present in a string. 
#It is used for caseless matching, i.e. ignores cases when comparing.
#For example, German lowercase letter ß is equivalent to ss. However, since ß is already 
#lowercase, lower() method does nothing to it. But, casefold() converts it to ss.

s1="PYTHON IS AWESOME"
s2=s1.casefold()
print(s2)

s3="der Fluß"
print(s3.casefold())