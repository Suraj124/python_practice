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

#maginitude
aa=np.array([1,2])
mag_a=np.linalg.norm(aa)
print("Magnitude of a is",mag_a)
# print(np.sqrt((aa*aa).sum()))

#angle between two vectors

x=np.array([1,2])
y=np.array([3,4])

cosangle=(x.dot(y))/(np.linalg.norm(x)*np.linalg.norm(y)) #cosangle is already in redian
print('Cos angle between x and y is',cosangle,np.degrees(cosangle))

#Diagonal of matrix

print("Diagonal elements",np.diag(a))

#Creating matrix with element 1,2,3 and other with 0

print(np.diag([1,2,3]))

print("Sum of diagonal elements",np.diag(a).sum(),np.trace(a))

