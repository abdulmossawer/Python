import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {"Days": [1, 2, 3, 4, 5],
        "NOP": [50, 40, 60, 30, 44]}

# df = pd.DataFrame(data)
# sns.lineplot(data = data, x = "Days", y = "NOP")
# plt.show()


data2 = pd.read_excel("ESD.xlsx")
#print(data2.head(10))
color = sns.color_palette("GnBu")
sns.lineplot(data = data2, x = "Department", y = "Age", hue = "Ethnicity", palette = color)
plt.show()