import matplotlib.pyplot as plt
import pandas as pd

l = [1, 3, 4, 7, 12, 2, 8, 9, 24]
l1 = [2, 3, 4, 6, 3, 5, 7, 3, 6]

plot_values = [l, l1]
# plt.boxplot(plot_values)
# plt.show()

data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
#print(df)
plt.boxplot(df["Annual Salary"])
plt.show()