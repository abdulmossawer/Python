import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = sns.load_dataset("tips")

print(data)
gp = data.groupby("day").agg({"tip": "mean"})
sns.heatmap(gp)
plt.show()


data = pd.read_excel("ESD.xlsx")
print(data)

gp = data.groupby("Department").agg({"Annual Salary": "mean"})
sns.heatmap(gp)

plt.show()