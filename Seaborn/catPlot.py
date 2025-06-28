import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.catplot(data = data, x = "day", y = "tip", hue = "sex", kind = "violin")
sns.catplot(data = data, x = "day", hue = "sex", kind = "count")

plt.show()