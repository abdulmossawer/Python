import matplotlib.pyplot as plt

x = [1, 8, 4, 7, 3]
y = [11, 54, 7, 32, 6]

plt.subplot(1, 2, 1)
plt.title("Age")
plt.bar(x, y)


x = [47, 88, 45, 70, 34]
y = [111, 4, 47, 12, 99]

plt.subplot(1, 2, 2)
plt.title("Weight")
plt.plot(x, y)
plt.suptitle("Employee Data")
plt.savefig("sub.png") # For save any charts line bar pie for presentation 
plt.show()