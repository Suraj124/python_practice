import numpy as np

my_list=[1,2,3,4,5,6,7,8,9]
arr1=np.array(my_list)
print(arr1)

arr2=np.arange(25)
print(arr2)

arr3=np.arange(0,25,2)
print(arr3)

arr4=np.zeros(10)
print(arr4)

arr5=np.zeros((5,5))
print(arr5)

arr6=np.ones(10)
print(arr6)

arr7=np.ones((5,5))
print(arr7)

arr8=np.linspace(0,100,5)
print(arr8)

arr9=np.eye(4)
print(arr9)             #indentiy matrix 

print("\n\n")
#--------------------------------------------------------------#
#Random  numbers

arr10=np.random.rand(5)     #5 random numbers between 0 to 1
print(arr10)

arr11=np.random.rand(4,5)
print(arr11)

arr12=np.random.randn(4)    
print(arr12)

arr13=np.random.randn(3,3)
print(arr13)

print("\n\n")

arr14=np.random.randint(0,50,10) #10 rabdom numbers between 0 and 50
print(arr14)

print("Max element",arr14.max())
print("Min element",arr14.min())
print('Position of max element is',arr14.argmax())
print('Position of min element is',arr14.argmin())

#---------------------------------------------------------------------------#

print("Reshape() method")

print("Before shaping is",arr2)
arr15=arr2.reshape(5,5)
print("After shaping 5*5 matrix\n",arr15)

#-----------------------------------------------------------------------------#

print('Before shaping \n',arr7)
arr16=arr7.reshape(25)
print('After shapping',arr16)

#------------------------------------------------------------------------------#

