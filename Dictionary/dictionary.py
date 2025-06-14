# employeeData = {"Name": "Sadiq", "Age": 22, "Gender": "Male", "Is Employed": True, "Salary": 45000.50}
# print(employeeData)
# print(employeeData["Salary"])

# Iteration in Dictionaries
# student = {"name": "John", "age": 25, "Class": "5th", "Roll_no": 2}

# Printing all the key names one by one
# for x in student:
#     print(x)

# Printing all the value names one by one

# for x in student:
#     print(student[x])

# Using value function

# for x in student.values():
#     print(x)

# Using item function

# for x,y in student.items():
#     print(x, ":", y)


# Nested Dictionary

employeeData = {1:{"Name": "Sadiq", "Age": 22, "Gender": "Male"},
                2:{"Name": "Lisa", "Age": 21, "Gender": "Female"},
                3:{"Name": "Abdul", "Age": 22, "Gender": "Male"}}
print(employeeData[2]["Name"])