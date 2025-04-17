import pandas as pd

df = pd.read_csv("shopping_trends.csv")

df2 = df[['Payment Method','Purchase Amount (USD)']].groupby('Payment Method').sum()

print(df2)