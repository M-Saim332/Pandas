import pandas as pd
df=pd.read_csv("pokemon.csv")

print(df.mean(numeric_only=True))
 # Telling the pandas to work on the numeric data only
""" print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count()) """

#Single column
""" print(df["Height"].mean())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].sum())
print(df["Height"].count()) """

#Using the group by function
group=df.groupby("Type1")
print(group["Height"].mean())