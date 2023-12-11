import pandas
import pandas as pd
import numpy as np

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(df.columns)
print(df["Primary Fur Color"].value_counts())
df2[""] = df["Primary Fur Color"].unique()



df3 = pd.DataFrame(df2)
print(df3)
#df3 = df3.rename({"Primary Fur Color": "Fur Color"})
df3.columns = ["Fur Color","Count"]
print(df3)
