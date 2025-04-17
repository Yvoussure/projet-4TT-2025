import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shopping_trends.csv")

df2 = df.groupby('Location')['Purchase Amount (USD)'].sum()

# Customize the plot
plt.pie(df2, labels=df2.index, autopct='%1.1f%%')
plt.title("Montant des vente par localisation")

# Save the plot as a PNG image
plot_dir = "plot"
plot_file_name = "12_pandas_plot_localisation_purchase_amout.png"
plt.savefig(f"{plot_dir}/{plot_file_name}")
print(f"Plot saved as {plot_dir}/{plot_file_name}")
