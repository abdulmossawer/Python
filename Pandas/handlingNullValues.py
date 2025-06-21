import pandas as pd
import numpy  as np

data = pd.read_csv("company1.csv")
# print(data.isnull().sum())

# print(data.dropna())
# print(data)
# print(data["salary"].mean())
data["salary"] = data["salary"].replace(np.nan, 24400)
print(data)
# print(data.fillna(method = "bfill"))
print(data.fillna(method = "ffill"))