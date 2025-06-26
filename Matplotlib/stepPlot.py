import matplotlib.pyplot as plt
import pandas as pd

x = ["day1", "day2", "day3", "day4", "day5"]
y = [20, 55, 78, 99, 43]

# plt.step(x, y, where = "mid", marker = "*")
# plt.show()

data = pd.read_excel("expense3.xlsx")
df = pd.DataFrame(data)
print(df)

group = df.groupby("Category").agg({"Amount": "sum"})
print(group)

# Convert index (Category names) to x positions (0, 1, 2, ...)
x = range(len(group))
y = group["Amount"].values
labels = group.index.tolist()

# Create step plot
plt.step(x, y, where="post", marker="*")
plt.xticks(x, labels, rotation=45)
plt.title("Step Plot of Expense by Category")
plt.ylabel("Total Amount")
plt.xlabel("Category")
plt.tight_layout()
plt.show()