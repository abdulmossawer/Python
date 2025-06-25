import pandas as pd

# dict = {"Keys": ["k1", "k2", "k1", "k2"],
#         "Names": ["Tom", "Chris", "Danish", "Faiz"],
#         "Houses": ["Red", "Green", "Black", "Grey"],
#         "Grades": ["3rd", "4th", "1st", "2nd"]}

dict = {"Names": ["Tom", "Chris", "Danish", "Faiz"],
        "Houses": ["Red", "Green", "Black", "Grey"],
        "Grades": ["3rd", "4th", "1st", "2nd"]}

df = pd.DataFrame(dict)
print(pd.melt(df, id_vars=["Names"], value_vars=["Houses", "Grades"]))
print(pd.melt(df, id_vars=["Names"], value_vars=["Houses", "Grades"], var_name="House&Grades", value_name="Value"))

print(df.pivot(index="Keys", columns="Names", values=["Houses", "Grades"]))

