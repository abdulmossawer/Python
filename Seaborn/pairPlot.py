import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("iris")
# print(data)
# sns.pairplot(data, hue = "species")


df = pd.read_excel("ESD.xlsx")
sns.pairplot(data)
plt.show()