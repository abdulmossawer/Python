import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")

#sns.kdeplot(data = data, x = "total_bill", hue = "day")
#sns.kdeplot(data = data, x = "total_bill", hue = "day", palette = "GnBu", multiple = "stack")
sns.kdeplot(data = data, x = "total_bill", hue = "day", palette = "viridis", multiple = "fill")
plt.show()