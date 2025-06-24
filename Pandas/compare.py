import pandas as pd

data = {"Fruits": ["Apple", "Mango", "Kiwi", "PineApple"], 
        "Quantity": [10, 15, 5, 3],
        "Price": [100, 150, 1000, 45]}

df1 = pd.DataFrame(data)

df2 = df1.copy()
# print(df2)

df2.loc[0, "Quantity"] = 30
df2.loc[3, "Quantity"] = 13
df2.loc[0, "Price"] = 200
df2.loc[3, "Price"] = 300

print(df2)
print(df1.compare(df2))
