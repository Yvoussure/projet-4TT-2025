import pandas as pd

df = pd.read_csv("shopping_trends.csv")

print(df[['Location','Item Purchased','Category','Purchase Amount (USD)']].groupby(['Item Purchased','Category','Location']).sum())