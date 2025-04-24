import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Meteorite_Landings.csv")
df2 = df['year'].value_counts().sort_index(ascending=False).head()

# Create a bar plot of the meteorite fall counts by year
df2.plot(kind='bar', figsize=(10, 8))

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Count')
# Set the title
plt.title('Meteorite Fall Counts by Year')

# Save the plot as a PNG image
plot_dir = "plot"
plot_file_name = "09_pandas_plot_fall.png"
plt.savefig(f"{plot_dir}/{plot_file_name}")
print(f"Plot saved as {plot_dir}/{plot_file_name}")