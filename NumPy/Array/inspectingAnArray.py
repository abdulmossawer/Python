import numpy as np

arr = np.array([[10, 20, 30, 77],[40, 50, 60, 70], [90, 54, 63, 78]])
# arr = np.array([10, 20, 30, 77])
# print(arr[0:3])
# print(arr[::-1])
# print(arr[1:4])
# print(arr[:2])
print(arr[0,1:3])
print(arr[1,::4])
print(arr[2,1:4])


print (np.shape(arr)) #rows, columns
print (np.size(arr)) #number of elements
print (np . ndim(arr))
print(len(arr)) #number of nested values
print(type(arr)) #datatype of variable
print (arr.dtype) #datatype of array
# convert
print(arr)
print(arr.astype(float)) #conversion of datatype
print(arr.astype(str)) #conversion of datatype
print(arr.astype(int)) #conversion of datatype