# Implicit type

a = 23
b = 2.5
print(type(a))
print(type(b))

c = a + b
print(c)
print(type(c))

# Explicit type

i = "125"
j = 2.5
print(type(i))
print(type(j))

i = float(i)
print("After convertion",type(i))

k = i + j
print(k)
print(type(k))