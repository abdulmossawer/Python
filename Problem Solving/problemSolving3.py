# Conditional Statements

# Q1: Check if a number is positive, negative, or zero.

# num = int(input("Enter your number: "))

# if num > 0:
#     print("Possitive", num)
# elif num < 0:
#     print("Negative", num)
# else:
#     print("Zero", num)


# Q2: Take input for age and print child (<12), teen (13–19), adult (20+).

# age = int(input("Enter your age: "))

# if age < 12:
#     print("Child")
# elif age <= 19:
#     print("Teen")
# else:
#     print("Adult")


#Q3: Find if a year is a leap year or not.

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
