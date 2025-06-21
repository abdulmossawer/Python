import pandas as pd

# Creation of DataFrames

data = {"Name": ["Sadiq", "Ayaz", "Danish"],
        "Age": [22, 20, 23],
        "Salary": [25000, 15000, 20000]}

df = pd.DataFrame(data)
print(df)

print()

# Open Csv file
print()


data = pd.read_csv("C:/Users/SADIQ/Downloads/dummy_sales.csv")
print(data)

print()
# Open Excel file
print()

data = pd.read_excel("dummy_sales.xlsx")
print(data)