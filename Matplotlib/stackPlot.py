import matplotlib.pyplot as plt
import pandas as pd

days = [1, 2, 3, 4, 5, 6, 7]

np1 = [40, 10, 15, 5, 20, 35, 75]
np2 = [50, 25, 55, 4, 30, 60, 65]
np3 = [70, 60, 65, 55, 75, 85, 120]

plt.stackplot(days, np1, np2, np3, colors = ["yellow", "blue", "red"], labels = ["Week1", "Week2", "Week3"])
plt.legend()
plt.show()

data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
print(df.head(20))

grouped_by = df.groupby("Job Title").agg[{"Annual Salary":"sum"}]
plt.stackplot(grouped_by.index, grouped_by["Annual Salary"])
plt.show()