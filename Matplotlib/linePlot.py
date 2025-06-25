import pandas as pd
import matplotlib.pyplot as plt

x = ["D1", "D2", "D3", "D4", "D5"]
y = [350, 240, 425, 600, 501]
y1= [500, 600, 750, 555, 250]

plt.plot(x, y, marker = "o", ls = "--", color = "red", label = "Week1")
plt.plot(x, y1, marker = "*", ls = "-", color = "green", label = "Week2", alpha = 0.5)
plt.xlabel("Opening Days", fontsize = 20)
plt.ylabel("Crowd In Bar", fontsize = 20)
plt.legend()
plt.show()


data = pd.read_excel("expense3.xlsx")
df = pd.DataFrame(data)
grouped_by = df.groupby("Category")["Amount"].sum()
print(grouped_by)
plt.plot(grouped_by.index, grouped_by.values)
plt.show()
