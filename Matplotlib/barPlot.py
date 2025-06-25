import matplotlib.pyplot as plt
import pandas as pd

# x = ["S1", "S2", "S3", "S4"]
# y = [75, 81, 98, 88]
# colors = ["yellow", "blue", "green", "orange"]
# plt.bar(x, y, color = colors, edgecolor = "black" )
# plt.xlabel("Seasons Of Panchayat", fontsize = 20)
# plt.ylabel("Popularity", fontsize = 20)
# plt.title("Popularity Of Different Seasons Of Panchayat", fontsize = 25)
# plt.show()


data = pd.read_excel("expense3.xlsx")
df = pd.DataFrame(data)

# print(df)
grouped_by = df.groupby("Payment Mode")["Amount"].sum()
print(grouped_by)
plt.bar(grouped_by.index, grouped_by.values)
plt.show()
