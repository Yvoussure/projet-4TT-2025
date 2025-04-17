import pandas as pd

df = pd.read_csv("shopping_trends.csv")

print(df[["Payment Method","Purchase Amount (USD)"]].groupby("Item Purchased").mean())