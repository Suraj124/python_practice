import numpy as np

arr=np.random.randint(1,100,10)

print('Square root',np.sqrt(arr))
print('\n')
print("sin",np.sin(arr))
print('\n')
print('Log',np.log(arr))
print('\n')
print("Sum of array",np.sum(arr),arr.sum())
print('\n')
print("Max element of array",arr.max(),np.max(arr))
print('\n')
print("Min element of array",arr.min(),np.min(arr))
print('\n')

#-------------------------------------------------------#
#Matrix
arr_2d=np.arange(1,26).reshape(5,5)
print('MAtrix is\n',arr_2d)

print('Max element in matrix',np.amax(arr_2d))
print('Min element in matrix',np.amin(arr_2d))
print("Max element in each row\n",np.amax(arr_2d,axis=1,keepdims=True))
print("Max element in each Column",np.amax(arr_2d,axis=0))
print("Min element in each row\n",np.amin(arr_2d,axis=1,keepdims=True))
print("Min element in each Column",np.amin(arr_2d,axis=0))
print('\n')

print("Mean",np.mean(arr_2d))   #can done along axis 0 or 1  ex->>np.mean(array,axis=0)

print("Median",np.median(arr_2d)) #can done along axis 0 or 1  ex->>np.median(array,axis=1)

#Standard deviation is the square root of the average of squared deviations from mean.
#std = sqrt(mean(abs(x - x.mean())**2))
print("Standard Deviation",np.std(arr_2d))

#Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2).
#  In other words, the standard deviation is the square root of variance.
print("Variance",np.var(arr_2d))

print("Average",np.average(arr_2d))

#Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1)
print("Weight mean",np.average([1,2,3,4],weights=[4,3,2,1]))
print("Weight mean",np.average([1,2,3,4],weights=[4,3,2,1],returned=True)) #return sum of weight