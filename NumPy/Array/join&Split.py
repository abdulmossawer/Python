# Join

import numpy as np

# arr1 = np.array([40, 50, 60])
# arr2 = np.array(([20, 30, 80]))
# print(np.concatenate([arr1, arr2]))

# arr1 = np.array([[40, 50, 60], [10, 70, 65]])
# arr2 = np.array(([[20, 30, 80], [58, 55, 35]]))
# print(np.concatenate([arr1, arr2]))

# Horizontal

# print(np.concatenate([arr1, arr2], axis=1))
# print(np.hstack([arr1,arr2]))

# Vertical

# print(np.concatenate([arr1, arr2], axis=0))
# print(np.vstack([arr1, arr2]))


# Split

# a = np.array([10, 20, 30, 40, 50, 60, 70])
a = np.array(([[20, 30, 80], [58, 55, 35]]))
b = np.array_split(a, 3)
print(b)
