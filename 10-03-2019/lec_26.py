lst=[333,-98,10.56,11.78,333]
print(lst)

#to remove all elements from list
# lst.clear()
# print(lst)

#maximum and minimum element in the list
print(max(lst))
print(min(lst))

#insert element in the list->>>> insert(position,object)
lst.insert(2,1024)
print(lst)

#sorting the list in ascending order
lst.sort()
print(lst)

#sorting in reverse order
lst.sort(reverse=True)
print(lst)

#count()
print(lst.count(333))