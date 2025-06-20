import numpy as np

# a = np.array([10,54,78,60])
# print(np.sum(a))
# print(np.max(a))
# print(np.min(a))
# print(np.mean(a))
# print(np.cumsum(a))
# print(np.cumprod(a))


a = (100,58,94,150, 235)
b = (2,6,7,5,4)

price = np.array(a)
quantity = np.array(b)

print(price, "\n", quantity)
print()
c = np.cumprod([price,quantity], axis=0)
print(c[1])
print(np.sum(c[1]))
