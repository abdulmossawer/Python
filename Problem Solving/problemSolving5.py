# 5. Functions

# Q1: Write a function to print "Hello, World!"

# def greet():
#     print("Hello World")
# greet()


# Q2: Function that returns square of a number.

# def sqr(n):
#     return n *n

# print(sqr(5))


# Q3: Function to check if number is prime.

def check_prime(num):
    if num == 1:
        print(num, ": It is not a prime number")
    if num == 2:
        print(num, ": It is a prime number")
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                print(num, ": It is not a prime number")
                break
        else:
            print(num, ": It is not a prime number")

check_prime(22)