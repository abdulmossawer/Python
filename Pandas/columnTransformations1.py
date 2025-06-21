import pandas as pd

df = pd.read_excel("ESD.xlsx")
# print(df)

df.loc[(df["Bonus %"] == 0), "GetBonus"] = "No Bonus"
df.loc[(df["Bonus %"] > 0), "GetBonus"] = "Bonus"
print(df["GetBonus"].head(10))


data = pd.read_excel("friends_employees.xlsx")
print(data)

data["Full Name"] = data["First name"].str.capitalize() + " " + data["Last Name"].str.capitalize()
print(data)
