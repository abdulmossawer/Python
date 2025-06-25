import matplotlib.pyplot as plt
import pandas as pd 

brands = ["Vivo", "Apple", "Samsung", "IQOO", "Xiaomi"]
x = [80, 12, 55, 90, 32]
c = ["blue", "grey", "silver", "yellow", "orange"]
ex = [0, 0, 0, 0.1, 0]
# plt.pie(x, labels = "brand", colors = c, explode = ex, startangle = 90, autopct = "2f", shadow = True)
# plt.show()


data = pd.read_excel("expense3.xlsx")
df = pd.DataFrame(data)

#print(df)
grouped_by = df.groupby("Payment Mode")["Amount"].sum()
print(grouped_by)
clr = ["silver", "yellow", "orange"]
exp = [0, 0, 0.1]
plt.pie(grouped_by.values, labels = grouped_by.index, autopct = "%2f", colors = clr, explode = exp, startangle = 90, shadow = True)
plt.show()