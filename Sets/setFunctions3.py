a = {"Ironman", "Captain", "Thor", "Loki"}
b = {"Batman", "Superman", "Wonder Woman"}
c = {"Thor", "Loki", "Spiderman"}

#Union

# print(a.union(c))

#Difference

# x = a.difference(c)
# print(x)

#Difference update

# a.difference_update(c)
# print(a)

#lntersection

# z = (a.intersection(c))
# print(z)

#lntersection Update

# a.intersection_update(c)
# print(a)

#Symmetric Difference

x = (a.symmetric_difference(c))
print(x)

#Symmetric Difference Update

a.symmetric_difference_update(c)
print(x)