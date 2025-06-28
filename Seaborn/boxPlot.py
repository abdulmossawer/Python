import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.boxplot(data = data, x = "day", y = "tip", hue = "sex", orient = "vertical", fliersize = 3, palette = "viridis")
plt.show()