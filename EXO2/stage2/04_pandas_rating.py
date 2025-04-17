import pandas as pd

df = pd.read_csv("shopping_trends.csv")

df2 = df[['Item Purchased', 'Review Rating']].groupby("Item Purchased").mean()

df2.sort_values("Review Rating", ascending=False, inplace=True)

print(df2)