# 1. Write a program to find max and min in a set.

# a = [88, 14, 22, 73, 614]
# maximum = max(a)
# minimum = min(a)
# print("Maximum of a", maximum)
# print("Minimum of a", minimum)

# 2. Write a program to find common elements in three lists using sets.

# a = [88, 14, 22, 73, 614]
# b = [14, 54, 36, 547, 73]
# c = [14, 42, 3, 65, 47, 22]
# print(set(a) & set(b) & set(c))

# 3. Write a program to find difference between two sets.

# a = {88, 14, 22, 73, 614}
# b = {14, 54, 36, 547, 73}

# print(b.difference(a))
# x = a.difference(b)
# print(x)

# 4. Write a Python program to remove an item from a set if it is present in the set.

# a = {88, 14, 22, 73, 614}
# a.remove(22)
# print(a)

# 5. Write a Python program to check if a set is a subset of another set.

a = {88, 14, 22, 73, 614, 547}
b = {14, 547, 73}
print(b.issubset(a))