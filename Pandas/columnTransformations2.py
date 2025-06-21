import pandas as pd

data = pd.read_excel("friends_employees.xlsx")
# print(data)

data["Bonus"] = (data["Salary"]/100)*20
print(data)


months = {"Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                    "October", "November", "December"]}

a = pd.DataFrame(months)

def extract(value):
    return value[0:3]

a["Short Monts"] = a["Months"].map(extract)

print(a)