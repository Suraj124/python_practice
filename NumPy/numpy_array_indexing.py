import numpy as np

arr=np.random.randint(1,50,10)
print(arr)
print("Element at position 5 is ",arr[5])   #indexing

print("Element index 2 to 5 is",arr[2:6])
print(arr[:4])
print(arr[7:])
print(arr[:-5:-1])

#-----------------------------------------------------------#
print('\n\n')
#we can assign a particular number to a sliced array but it will also affect original arrray
slice_array=arr[0:5]
slice_array[:]=12
print(slice_array)
print(arr)

#to resolve this problem we hace to copy the original array

slice_array=arr.copy()
slice_array[:]=25
print(slice_array)
print(arr)
print('\n\n\n\n\n')
#-------------------------------------------------------------------------------------#
#Matrix:->>>>

arr_2d=np.array([[10,23,31],[55,19,90],[25,52,11]])
print(arr_2d)

print("First row",arr_2d[0])    #printing 1st row
print("Element at row 1 and col 2 is",arr_2d[0,1])
print("Element at row 3 and col 1 is",arr_2d[2][0])

#slicing of matrix
print("slicing of matrix")

print("Original amatrix\n",arr_2d)
print('\n')
print(arr_2d[:2,1:])
print('\n')
print(arr_2d[1:,1:])
print('\n')
print(arr_2d[1:,:2])

#----------------------------------------------------------#
#Transpose of matrix
t_mat=arr_2d.T
print('Transpose Matrix\n',t_mat)

#----------------------------------------------------------#
#Inverse of matrix
mat_inv=np.linalg.inv(arr_2d)
print('Inverse of Matrix\n',mat_inv)
print(mat_inv.dot(arr_2d))

#-------------------------------------------------------#
print('\n\n\n\n')
#Conditional array

# bool_arr=arr>20
# print(bool_arr)
# print(arr[bool_arr])
print(arr)
print("Array having more than 20",arr[arr>20])


