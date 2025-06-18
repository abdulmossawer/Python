# Local Var

# x = 12
# print("First value of x :", x)
# def hello():
#     x = 15
#     return x
# print(hello())
#
# print(x)


# Global Var

x = 12
print("First value of x :", x)
def hello():
    global x
    x = 15
    return x
print(hello())

print(x)