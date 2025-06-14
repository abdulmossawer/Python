# Write a python program to sort a dictionary by value.

# a = {"a": 8, "b": 2, "c": 4, "d": 1, "e": 5}
# a = sorted(a.values())
# print(a)


# Write a python script to print a dictionary where the keys are
# numbers between 1 and 15 and the values are square of keys.

# a = {}
# for i in range(1,21):
#     a[i] = i*i
# print(a)


# Write a program to multiply all the items in a dictionary.

a = {"a": 8, "b": 2, "c": 4, "d": 1, "e": 5}
product = 1
for i in a:
    product *= a[i]
print(product)


# Write a python program to sort a dictionary by key.

# a = {5:"a", 2:"b", 33:"c", 4:"d", 87:"e", 55:"f", 1:"g"}
# a = sorted(a.keys())
# print(a)