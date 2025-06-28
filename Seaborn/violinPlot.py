import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data = sns.load_dataset("tips")
# print(data)
# sns.violinplot(data = data, x = "tip", hue = "sex")
# plt.show()


df = pd.read_excel("ESD.xlsx")
print(df)
sns.violinplot(data = df, x = "Annual Salary")
plt.show()