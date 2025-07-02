import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.swarmplot(data = data, x = "day", y = "total_bill", hue = "sex", dodge = True)
plt.show()