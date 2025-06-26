import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

x = np.random.randint(1, 100, size = 30)
plt.stem(x, linefmt = "--", markerfmt = "*", orientation = "horizontal")
plt.title("Stem Plot of Random Values")

data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
df2 = df.head(50)
plt.stem(df2["Age"], markerfmt = "D")
plt.plot(df2["Age"])
plt.show()