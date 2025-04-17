import pandas as pd

df = pd.read_csv("shopping_trends.csv")

df2 = df[['Location','Item Purchased','Payment Method','Purchase Amount (USD)']].groupby('Location','Payment Method').sum()

print(df2)