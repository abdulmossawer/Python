# For loop
# for i in range(1,6):
# for i in range(1,11,2):
# for i in range(0,11,2):
#     print(i)

# Table in For loop
# n = int(input("Enter a number : "))
# # for i in range(0,11,2):
# for i in range(1,11,2):
#     print(n, "*", i, "=", n * i)


# While loop
# n = 1
# while n<=5:
#     print(n)
#     # n +=1
#     n += 2

# Table in While loop
# n = 1
# a = int(input("Enter a number: "))
# while n<=10:
#     print(a, "*", n, "=", a*n)
#     n += 1
#     # n += 2


# While true
# n = 1
# while True:
#     print(n)
#     n += 1

# while True:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     print(num1 + num2)
#     repeat = input("Do you want to repeat it?: ")
#     if repeat == "yes" or "Yes" or "YES":
#         break


# Nested loop
# for i in range(1,11):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# For Loop with Conditional Statements
# for i in range (1,6):
#     if i == 3:
#         print(i, "This is my favourite song")
#     else:
#         print(i)

# for i in range(1,101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)

# While Loop with Conditional Statements
# n = 1
# while n<=5:
#     if n == 3:
#         print("This is my favourite song")
#     else:
#         print(n)
#     n += 1

# n = 1
# while n <=100:
#     if n % 8 == 0 and n % 12 == 0:
#         print(n)
#     n += 1


# Continue Statement
# for i in range(1, 9):
#     if i == 5:
#         continue
#     else:
#         print(i)

# n = 1
# while n <= 9:
#     if n == 5:
#         n +=1
#         continue
#     else:
#         print(n)
#     n +=1

# Break Statement
# for i in range(1, 9):
#     if i == 5:
#         break
#     else:
#         print(i)

n = 1
while n <= 9:
    if n == 7:
        n +=1
        break
    else:
        print(n)
    n +=1
