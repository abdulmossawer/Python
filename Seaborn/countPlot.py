import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data = sns.load_dataset("tips")
# #print(data)
# sns.countplot(data = data, x = "sex", hue = "smoker", palette = "viridis")
# plt.show()


data = pd.read_excel("ESD.xlsx")
print(data)
sns.countplot(data = data, x = "Business Unit", hue = "Department", palette = "GnBu")
plt.show()