'''
1->Counter(any list)
2->c.most_common(para)
3->c.clear()
4->c.itms(),
5->list(c),dict(c),set(c)
6->sum(c.values())
'''
from collections import Counter
l=[1,2,3,4,5,6,1,2,3,4,3,2,3,4,5,6,7,8,89,9,0,8,7,6,5,4,4,2,34,5,6]
print(Counter(l))

l1='ancdeabvdfvferhcbvdgstcvdvrdtcdfvde'
print(Counter(l1))

word='My name is this and this i my name for you and that it\'s '
my_word_list=word.split(" ")
print(Counter(my_word_list))
#---------------------------------------------------------#

#### most_common(para) --> para indicate how many common words you want####

c=Counter(my_word_list)
print("Most common words are",c.most_common(3))
print("Least common words are",c.most_common(3)[:-3-1:-1])

#------------------------------------------------------------#

####    sum(c.values())     ####

print("Total elements are",sum(c.values()))

#-----------------------------------------------------#

#c.clear()  -->reset all counts

# c.clear()
# print(c.items())

#-------------------------------------------------------------------#

#list(c)    -->list unique elements

print(list(c))

#------------------------------------------------------------------#

#set(c) -->Convert to a set

print(set(c))

#-----------------------------------------------------------------#

#dict(c)    -->convert to a dictionary

print(dict(c))

#---------------------------------------------------------------#

#c.items()  --> convert into a pairs (key, value)

for i,j in c.items():
    print(i,"   =   ",j)

for i,j in Counter(input("Enter a string : ").split(' ')).items():
     print(i,'occur',j,'times')