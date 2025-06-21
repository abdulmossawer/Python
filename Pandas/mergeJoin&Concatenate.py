import pandas as pd

# Merge

data1 = {"Emp Id": ["E01", "E02", "E03", "E04", "E05", "E06"],
        "Name": ["Sadiq", "Fareed", "Faiz", "Danish", "Saad", "Ayaz"],
        "Age": [22, 21, 23, 24, 25, 20]}

# data2 = {"Emp Id": ["E01", "E02", "E03", "E04", "E05", "E06"],
#         "Salary": [70000, 90000, 80000, 35000, 60000, 50000]}

data2 = {"Emp Id": ["E01", "E02", "E07", "E04", "E08", "E09"],
        "Salary": [70000, 90000, 80000, 35000, 60000, 50000]}

dm1 = pd.DataFrame(data1)
dm2 = pd.DataFrame(data2)

# print(dm1)
# print(dm2)

# print(pd.merge(dm1, dm2, on = "Emp Id"))
print(pd.merge(left = dm1, right= dm2, on = "Emp Id", how = "left"))
print(pd.merge(left = dm1, right= dm2, on = "Emp Id", how = "right"))

