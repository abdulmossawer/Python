# Return

# def hello():
#     return("Hello World")
# print(hello())
#
# def add(a, b):
#    return(a + b)
# print((add(6,25)))


# Recursion
# def hello():
#     print("Hello")
#     return hello()
# print(hello())

def fact(n):
   if n == 0:
       return 1
   else:
       return n * fact(n-1)

print(fact(6))