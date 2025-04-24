import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Meteorite_Landings.csv")
df2 = df['recclass'].value_counts().sort_values(ascending=False).head(14)

# Create a bar plot of the meteorite fall counts by year
df2.plot(kind='bar', figsize=(10, 8))

# Set the labels and title
plt.xlabel('Class')
plt.ylabel('Count')
# Set the title
plt.title('Top 14 Meteorite Classes by Count')

# Save the plot as a PNG image
plot_dir = "plot"
plot_file_name = "10_pandas_plot_top14.png"
plt.savefig(f"{plot_dir}/{plot_file_name}")
print(f"Plot saved as {plot_dir}/{plot_file_name}")