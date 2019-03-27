st={1,4,2,7,4}
print(st)
st1=frozenset(st)
# st1.add("python")     we can not add elements in frozen set
# st1.remove(1)         we can not delete elements from frozen set
print(st1)