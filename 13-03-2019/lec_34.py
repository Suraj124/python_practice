dic1={1:"Jhon",2:"Bob",3:"William"}
print(dic1)
########################################################
# key=dic1.keys()
# # print(type(key))
# for i in key:
#     print(i)

# value=dic1.values()
# # print(type(value))
# for i in value:
#     print(i)
###########################################################
# print(dic1[2])      #we can access dictionary directly

# del dic1[2]     #delete 2 dictionary value

# print(dic1)
#####################################################
# for i,j in dic1.items():
#     print(i,j)

# if "Jhon" in dic1.values():
#     print("Yes")
# else:
#     print("NO")

# if "Suraj" in dic1.values():
#     print("No")
# else:
#     print("No")

################################################  Adding new item to dictionary    ###########################################

dic1[4]="Smith"
print(dic1)

################################################ Removing item from dictionary     #########################################

dic1.pop(2)
print(dic1)