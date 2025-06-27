import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)
sns.scatterplot(data = data, x = "total_bill", y = "tip", hue = "day", size = "size", palette = "muted")
plt.show()