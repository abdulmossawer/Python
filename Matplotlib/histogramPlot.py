import matplotlib.pyplot as plt
import pandas as pd

x = [12, 1, 47, 65, 65, 44, 67, 12, 34, 77, 77, 77, 65, 88, 3, 5, 6, 4, 15, 12, 19, 25, 29, 90, 90, 90, 90, 95, 100, 35, 87]
#plt.hist(x, bins = 10, color = "green", edgecolor = "red")
#plt.show()

data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
plt.hist(df["Age"], bins=10)
plt.show()