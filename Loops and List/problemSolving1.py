# For Loop
# Print the square of numbers from 1 to 10 using a for loop
# for i in range(1,11):
#     print(i,"Square",i*i)

# Print all even numbers between 20 and 40 using a for loop.
# for i in range(20, 41, 2):
#     print(i)


# While Loop
# Print numbers from 10 to 1 in reverse using a while loop.
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# Print the sum of numbers from 1 to 50 using a while loop.
# i = 1
# total = 0
# while i <= 50:
#     total += i
#     i += 1
# print("Sum:", total)


# Nested Loops
# Multiplication tables from 2 to 5
# for i in range(2, 6):
#     print(f"Table of {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()


# For Loop with Conditional Statements
# Print numbers from 1 to 30 that are divisible by 3 but not by 6.
# for i in range(1, 31):
#     if i % 3 == 0 and i % 6 != 0:
#         print(i)

#  Print all numbers between 10 and 50 that are prime.
# for num in range(10, 51):
#     is_prime = True
#     if num < 2:
#         is_prime = False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# Break and Continue Statements
# Print numbers from 1 to 20 but stop the loop if the number is divisible by 7.
# for i in range(1, 21):
#     if i % 7 == 0:
#         break
#     else:
#         print(i)

#  Print numbers from 1 to 10, skipping number 4 and 6 using continue.
# for i in range(1, 11):
#     if i == 4 or i == 6:
#         continue
#     print(i)


# Write a program to display this pattern.
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# Write a program to display this pattern.
# 11111
# 2222
# 333
# 44
# 5

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i,end=" ")
#     print()


# Write a program to display this pattern.
#      *
#     **
#    ***
#   ****
#  *****

# for i in range(1,6):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()


# Write a program to display this pattern.
# 1
# 21
# 321
# 4321
# 54321

# for i in range(1,6):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()


# Write a program to display this pattern.
# *
# **
# ***
# ****
# *****
# ***
# **
# *

# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
# for i in range(5, 0, -1):
#     for k in range(0, i-1):
#         print("*", end="")
#     print()


# Write a program to display this pattern.
# 1
# 3 6 9
# 4 8 12 16
# 5 IO 15 20 25
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
# 9 18 27 36 45 54 63 72 81
# 10 20 30 40 50 60 70 80 90 100

for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()