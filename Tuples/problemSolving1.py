# 🟢 Beginner Level (Basic Operations)
# 1. Create a tuple with 5 different data types.
# → Expected: Use int, str, float, bool, list inside a tuple.

# a = (1, "Apple", 22.6, True, ["Mango", "Orange"])
# print(a)

# 2. Access the 3rd element of the tuple (10, 20, 30, 40, 50)
# → Expected output: 30

# a = (10, 20, 30, 40, 50)
# print(a[2])

# 3. Slice the tuple (1, 2, 3, 4, 5, 6) to get (3, 4, 5)

# a = (1, 2, 3, 4, 5, 6)
# print(a[2:5])
# print(a[2:-1])

# 4. Count how many times 2 appears in the tuple (1, 2, 3, 2, 4, 2, 5)

# a = (1, 2, 3, 2, 4, 2, 5)
# print("Count how many times 2 appears in the tuple: ", a.count(2))

# Check if "apple" is present in the tuple ("banana", "cherry", "apple", "grape")

# a = ("banana", "cherry", "apple", "grape")
# print("apple" in a)


# 🟡 Intermediate Level (Conversions & Nesting)
# 6. Convert a list [10, 20, 30] into a tuple.

# a = [10, 20, 30]
# print("Before coversion list: ", type(a))
# print(a)
# a = tuple(a)
# print("After coversion list: ", type(a))
# print(a)

# 7. Swap the values of two variables using a tuple.
# Example: a = 5, b = 10 → swap using tuple unpacking.

# a = 5
# b = 10
# print("a:", a)
# print("b:", b)
# a, b = b, a
# print("After swapping")
# print("a:", a)
# print("b:", b)

# 8. Loop through a tuple and print each element on a new line.

# a = (1, "Mango", False, ["Banana", "Kiwi"])
# for i in a:
#     print(i)

# i = 0
# for i in range(len(a)):
#     print(a[i])

# while i < len(a):
#     print(a[i])
#     i = i + 1

# 9. Create a nested tuple: ("person", (25, "male")) and access the value male

# a = ("person", (25, "male"))
# print(a[1][1])


# 🔴 Advanced Level (Tuple Use Cases)
# 10. Given list of student tuples, print student with highest score

students = [("Ayaz", 85), ("Abdul", 92), ("Ali", 78)]
top_student = max(students, key=lambda x: x[1])
print("Top student:", top_student)
