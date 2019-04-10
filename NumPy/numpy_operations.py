import numpy as np

arr=np.arange(11)
print('Array with 1 to 10',arr)

print('Multiplication',arr*arr)
print('\n')
print('Addition',arr+arr)
print('\n')
print('Substraction',arr-arr)
print('\n')
print('Multiply with 2',arr*2)
print('\n')
print('Power 2',arr**2)
print('\n')

print('An array with 10 5s',np.ones(10)*5)
print('\n')
arr2=np.arange(10,21)
print('Array with 10 to 20',arr2)
print("Horizontal append",np.hstack((arr,arr2)))
print("Vertical append append\n",np.vstack((arr,arr2)))

#-----------------------------------------------------------#
print('\n')
#Oparation on matrix
print("Oparation on matrix")

arr_2d=np.arange(1,26).reshape(5,5)
print(arr_2d)

print("Multiplt by 2\n",arr_2d*2)


print('Coloumn sum',np.sum(arr_2d,axis=0))
print('ROw sum',np.sum(arr_2d,axis=1))


