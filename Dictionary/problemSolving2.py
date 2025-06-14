# Convert the following dictionary into JSON format.
import json

# student_data = {"name": "Sadiq", "age": 22, "gender": "Male"}
# print(type(student_data))
# data = json.dumps(student_data)
# print(data)
# print(type(data))


# Access the value of age from the given data.

# student_data = """{"name": "Sadiq", "age": 22, "gender": "Male"}"""
# print(type(student_data))
# data = json.loads(student_data)
# print(type(data))
# print(data["age"])


# Pretty Print following JSON data.

# data = json.dumps(student_data, indent=4, separators=(",", "="))
# print(data)


# Sort the following JSON keys and write them into a file.

# f = open("demo.json", "w")
# data = json.dumps(student_data, indent=4, sort_keys=True)
# f.write(data)
#
# print("Data written to demo.json")


# Access the nested key "marks" from the following nested data
student_data = """{ "student":
                    {"grade": 
                      {"name":"David","marks":99 }
                      }
}"""

data =  json.loads(student_data)
print(data["student"]["grade"]["name"])

