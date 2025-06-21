import pandas as pd


data = pd.read_excel("ESD.xlsx")
#print(data.head(5))

gp = data.groupby(["Department", "Gender"]).agg({"Gender": "count"})
#print(gp)

#gp1 = data.groupby(["Country", "City"]).agg({"Age":"mean"})
#gp1 = data.groupby(["Country", "City"]).agg({"Annual Salary":"mean"})
#gp1 = data.groupby(["Country", "City"]).agg({"Annual Salary":"max"})
gp1 = data.groupby(["Country", "City"]).agg({"Bonus %":"min"})

print(gp1)