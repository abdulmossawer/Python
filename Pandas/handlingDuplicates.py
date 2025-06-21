import pandas as pd

data = pd.read_csv("company1.csv")
print(data)

# print()

print(data.drop_duplicates("EEID"))

# print(data["EEID"].duplicated().sum())

