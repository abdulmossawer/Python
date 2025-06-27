import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")
print(data)

sns.histplot(data = data, x = "age", hue = "alive", kde = True, discrete = True)
plt.show()