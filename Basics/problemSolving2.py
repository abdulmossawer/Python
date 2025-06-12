#Write a program to check if a number is positive.
# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive")
# else:
#     print("The number is negative")


#Write a program to check whether a number is odd or even.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")


#Write a program to create area calculator
# print("*****AREA CALCULATOR*****")
# print("""Press 1 to calculate the area of square
# Press 2 to calculate the area of rectangle
# Press 3 to calculate the area of circle
# Press 4 to calculate the area of triangle""")
#
# choice = int(input("Enter your choice 1-4: "))
#
# if choice == 1:
#     side = float(input("Enter side length: "))
#     area = side ** 2
#     print("The area of square is: ",area)
#
# elif choice == 2:
#     length = float(input("Enter length of rectangle: "))
#     width = float(input("Enter width of rectangle: "))
#     area = length * width
#     print("The area of rectangle is: ",area)
#
# elif choice == 3:
#     radius = float(input("Enter radius of circle: "))
#     area = ((22/7)*(radius**2))
#     print("The area of circle is: ",area)
#
# elif choice == 4:
#     base = float(input("Enter base of triangle: "))
#     height = float(input("Enter height of triangle: "))
#     area = 0.5 * base * height
#     print("The area of triangle is: ",area)
#
# else:
#     print("Invalid choice")


#Write a program check whether the passed Letter is a vowel or not.
# letter = input("Enter a letter: ")
# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("Vowel")
# else:
#     print("Don't Vowel")

#Write a program to check if a number is a single digit number,
#2-digit number and so on... , up to 5 digits.
num = int(input("Enter a number here up to 5 digits: "))

if num >= 0 and num <= 9:
    print("it's a single digit number")

elif num >= 10 and num <= 99:
    print("it's a double digit number")

elif num >= 100 and num <= 999:
    print("it's a triple digit number")

elif num >= 1000 and num <= 9999:
    print("it's a four digit number")

else:
    print("it's a five digit number")
