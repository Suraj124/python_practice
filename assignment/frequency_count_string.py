st="ABC ABC abc abc A a"
l1=[]
l2=[]
for i in range(len(st)):
    if st[i] not in l1:
        c=st.count(st[i])
        l1.append(st[i])
        l2.append(c)
for i in range(len(l1)):
    print(l1[i],l2[i])