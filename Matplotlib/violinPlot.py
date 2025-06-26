import matplotlib.pyplot as plt
import pandas as pd

x = [11, 2, 25, 14, 14, 14, 14, 19, 20, 28, 33, 55, 88, 100, 95, 95]
# print(len(x))
# plt.violinplot(x, showmeans = True)
# plt.show()

data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
#print(df)
plt.violinplot(df["Annual Salary"], showmedians = True)
plt.show()
