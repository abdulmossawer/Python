# Loops

# Q1: Print numbers from 1 to 10 using a while loop.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# Q2: Print the multiplication table of 7 using a for loop.

# for i in range(1, 11):
#     print(f"7 * {i} = {7*i}")


# Q3: Calculate the sum of all even numbers between 1 to 100.

total = 0
for i in range(2, 101, 2):
    total += i
print("Sum =", total)
