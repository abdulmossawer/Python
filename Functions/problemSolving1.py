# Write a function to find maximum of three numbers in Python.

# def maximum_num(val1,val2,val3):
#     if val1 > val2 and val1 > val3:
#         print("The greatest number is val1 :", val1)
#
#     elif val2 > val1 and val2 > val3:
#         print("The greatest number is val2 :", val2)
#
#     else:
#         print("The greatest number is val3 :", val3)
#
# maximum_num(44,250,9)


# Write a Python function to create and print a list where the
# values are square of numbers between 1 and 30.

# def create_list():
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     return l
#
# print(create_list())


# Write a Python function that takes a number as a parameter
# and check if the number is prime or not.

# def check_prime(num):
#     if num == 1:
#         print(num, ": It is not a prime number")
#     if num == 2:
#         print(num, ": It is a prime number")
#     if num > 2:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(num, ": It is not a prime number")
#                 break
#         else:
#             print(num, ": It is not a prime number")
#
# check_prime(22)


# Write a Python function to sum all the numbers in a List.

def add(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return(total)

print("Total numbers of sum is :", add([2,5,8]))

# (Using Recursion)

def add(numbers):
    if len(numbers) == 1:
        return (numbers[0])
    else:
        return (numbers[0]) + add(numbers[1:])

print("Total numbers of sum is :", add([2,5,8]))


# Write a Python program to solve the Fibonacci Sequence using recursion

def fib(num):
    if num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        return (fib(num - 1) + fib(num - 2))

print(fib(22))