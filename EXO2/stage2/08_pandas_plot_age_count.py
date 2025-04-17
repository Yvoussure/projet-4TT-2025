import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("shopping_trends.csv")

# Cout the occurences of each item
item_counts = df['Item Purchased'].value_counts()

item_counts.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Item')
plt.ylabel('Count')
plt.title('item value Counts')

plt.savefig('plot/08_pandas_plot_age_count.png')