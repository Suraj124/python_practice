import numpy as np

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print('Dot ptoduct of a and b is\n',a.dot(b),"\n\n",np.dot(a,b))
print(np.vdot(a,b))

#Determinants
det_a=np.linalg.det(a)
print('Determinant of a is',det_a)

det_b=np.linalg.det(b)
print('Determinant of a is',det_b)

#Inverse
inv_a=np.linalg.inv(a)
print("Inverse of a is \n",inv_a)