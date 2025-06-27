import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)
#data2 = data.head(10)
sns.barplot(data = data, x = "day", y = "tip", hue = "sex", order = ["Sat", "Sun", "Fri", "Thur"], palette = "viridis", errorbar = ("ci", 0))
plt.show()