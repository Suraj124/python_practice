import re

text="This is a string with term1 but not with term"

patterns=['term1','term2']

for pattern in patterns:
    print("Looking for",pattern,"in :\n",text)
    if re.search(pattern,text):
        print("Match Found")
    else:
        print("Match not found")

match=re.search(pattern[0],text)
print(match)

#This Match object returned by the search() method is more than just a Boolean or None, 
# it contains information about the match, including the original input string, the regular 
#expression that was used, and the location of the match. Let's see the 
#methods we can use on the match object:

print(match.start())
print(match.end())

#------------------------------------------------------------------------------------------------------#

#re.split(split_term,any_string)

res=re.split('@','Python@Programming and java @Programming')
print(res)