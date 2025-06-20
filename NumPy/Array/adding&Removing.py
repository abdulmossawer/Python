import numpy as np

# Add

# a = np.array([10,20,30,40,50])
# print(np.append(a, [60,70]))

# a = np.array([[10, 20], [30, 40]])
# print(np.insert(a, 1, 60))                #array,index,values
# print(np.insert(a, 0, [70,80], axis=0))
# print(np.insert(a, 2, [70,80], axis=1))


# Remove

# a = np.array([10,20,30,40,50])
# b = np.delete(a,1)

a = np.array([[10, 20], [30, 40]])
print(a)
b = np.delete(a,1, axis=0)
print(b)
b = np.delete(a,0, axis=1)
print(b)