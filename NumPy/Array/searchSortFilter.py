import numpy as np

# Sort

# a = np.array([8,5,9,2,7])
# print(np.sort(a))

# a = np.array([[8,5,9,2,7], [9,5,4,3,6]])
# print(np.sort(a))


# Search

# a = np.array([8,5,9,2,7])
# s = np.where(a == 9)
# print(s)
# s = np.where(a>4)
# print(s)
# s = np.where(a % 2 == 0)
# print(s)

# Sorted Search

# a = np.array([1,3,4,5,8])
# ss = np.searchsorted(a,4)
# print(ss)


# Filter

a = np.array([8,5,9,2,7])

# fa = [False, True, True, False, True]
# new = a[fa]
# print(new)

# fa = a > 5
# fa = a >= 5
# fa = a % 2 == 0
fa = a % 2 == 1
new = a[fa]
print(new)
