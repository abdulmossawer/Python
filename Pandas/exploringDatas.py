import pandas as pd

data = pd.read_excel("ESD.xlsx")
# print(data)
# print(data.head(10))
# print(data.tail(10))
# print(data.info())
e = data.describe()
print(e)
# print(data.isnull().sum())