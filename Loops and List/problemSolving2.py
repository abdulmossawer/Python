# Write a program to get Fibonacci series up to 10 numbers.

# a = 0
# b = 1
# n = int(input("Enter a number: "))
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


# Write a program to check if a number is prime or not.

# num = int(input("Enter a number: "))
# if num <= 1:
#     print("It's not a prime number.")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("It's not a prime number.")
#             break
#     else:
#         print("It's prime number.")


# Write a program to find a palindrome of integers.

# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while num > 0:
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10
#
# if rev == temp:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")


# Take an input from a user as a string then, reverse it.

# a = input("Enter anything:")
# print(a[:: - 1])


# Write a program to check if a string contains only digits.

# a = input("Enter anything:")
# b = (a.isdigit())
# if b == True:
#     print("It contain's only digits")
# else:
#     print("It does not contain digits")


# Write a program to check if a string is palindrome.

# a = input("Enter anything:")
# rev = (a[::-1])
# if rev == a:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")


# Write a program to find number of vowels in a string.

# a = input("Enter anything:")
# vowels = 0
# for i in a:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         vowels += 1
# print("The number of vowels is:",vowels)


# Write a program to check if every word in a string begins with a capital letter.

# a = input("Enter anything:")
# b = (a.istitle())
# if b == True:
#     print("It contains capital letters")
# else:
#     print("It does not contain capital letters")