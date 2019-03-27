import pickle,lec_142
f=open("student.dat","wb")
s=lec_142.Student(123,"Smith",450)
pickle.dump(s,f)
f.close()