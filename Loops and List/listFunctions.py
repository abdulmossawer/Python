# to find the Length of a List
from itertools import count

# a = ["Thor", "Sentry", "Spiderman", "Hulk", "Sentry"]
# print(len(a))


# to count an occurence of a particular element

# print(a.count("Sentry"))


# to add to the List

# a.append("Ironman")
# print(a)


# to add to a specific Location

# a.insert(0,"Groot")
# print(a)


# to remove from a List

# a.remove("Groot")
# print(a)


# to remove from a certain Location

# a.pop(3)
# print(a)


# to create a copy of a List

a = ["Thor", "Sentry", "Spiderman", "Hulk", "Groot"]
# print("a:", a)
# b = a.copy()
# print("Copy of a:",b)

# to access an element

# print(a.index("Hulk"))


# to extend the List

# c = ["Ironman", "Vision"]
# print(c)
# a.extend(c)
# print(a)


# to reverse the List

# a.reverse()
# print(a)


# to sort the List

# a.sort()
# print(a)

# to clear all the data from the List

# print("Without clear the list :", a)
# a.clear()
# print("Cleared the list :", a)


# List comprehension
l1 = [30, 40, 50, 60, 70]
print("L1 :", l1)
l3 = [i for i in l1 if i > 45]
print("L3 :", l3)
