import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("shopping_trends.csv")

# Cout the occurences of each item
df2 = df[['Review Rating','Item Purchased']].groupby('Item Purchased').mean()
df2.sort_values('Review Rating', ascending=False, inplace=True)

df2.plot(kind='bar', figsize=(10, 6))

plt.xlabel('item')
plt.ylabel('Rate')
plt.title('item review rating')

plt.savefig('plot/09_pandas_plot_item_review_rating.png')