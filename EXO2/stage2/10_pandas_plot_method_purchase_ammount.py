import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("shopping_trends.csv")
df2 = df[['Payment Method','Purchase Amount (USD)']].groupby('Payment Method').sum()

fig, ax = plt.subplots(figsize=(10, 10))
df2.plot(kind='bar', ax=ax)

for i, v in enumerate(df2["Purchase Amount (USD)"]):
    ax.text(i, v, str(v), ha='center', va='bottom')

plt.xlabel('Payment Method')
plt.ylabel('Purchase Amount')
plt.title('Sum purchase amount by payment method')

plt.savefig('plot/10_pandas_plot_method_purchase_ammount.png')