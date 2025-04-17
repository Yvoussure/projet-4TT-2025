import pandas as pd

df = pd.read_csv("shopping_trends.csv")

df2 = (df["Payment Method"].unique())

i = 0

for i, elm in enumerate(df2):
    i += 1
    print(f"{i}. {elm}")