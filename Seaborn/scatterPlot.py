import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data = sns.load_dataset("tips")
# print(data)
# sns.scatterplot(data = data, x = "total_bill", y = "tip", hue = "day", size = "size", palette = "muted")
# plt.show()

data = pd.read_excel("ESD.xlsx")

#print(data)
sns.scatterplot(data = data, x = "Age", y = "Annual Salary", size = "Bonus %", hue = "Department")
#plt.legend(bbox_to_anchor = (0.2, 0, 1.2, 1))
plt.show()