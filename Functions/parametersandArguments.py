def rect(height, width):
    print("the rect is:", height*width)
rect(14,8)

# Arbitrary arguments
def hello(*name):
    print("Hello my name is :", name[2])
hello("John", "Smith", "Lisa")