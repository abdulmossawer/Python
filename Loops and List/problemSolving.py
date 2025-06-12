# Write a program to find a sum of all the even numbers up to 50.
# sum = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# Write a program to write first 20 numbers and their squared numbers.
# for i in range(1,21):
#     print(i, "Square", i*i)


# Write a program to find sum of first 10 odd numbers  using while loop.
# sum = 0
# n = 0
# while n <= 20:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("The sum of first 10 odd numbers", sum)


# Write a program to check if a number is divisible by 8 and 12, up to 100 numbers
# for i in range(1,101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)


# Write a program to create a billing system at supermarket.
while True:
    name =  input("Enter your name: ")
    total = 0
    while True:
        print("Enter your amount & quantity")
        amount = float(input("Enter your amount: "))
        quantity = float(input("Enter your quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items? (y/n): ")
        if repeat == "N" or repeat == "n":
         break
    print("-"*40)
    print("Name:", name)
    print("Your total amount is:", total)
    print("-"*40)
    print("********** Thank you visit again ************")

    repeat1 = input("Do you want to go to next coustomer? (y/n): ")
    if repeat1 == "N" or repeat1 == "n":
        break






