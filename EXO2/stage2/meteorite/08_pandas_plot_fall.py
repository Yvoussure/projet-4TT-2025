import pandas as pd
import matplotlib.pyplot as plt

# Le nombre de météorites observées en train de tombé et celles découvertes plus tard

# Read the CSV file
df = pd.read_csv("Meteorite_Landings.csv")

# Group by 'fall' and count the number of occurrences
df2 = df.groupby('fall')['fall'].count()

# Customize the plot
plt.pie(df2, labels=df2.index, autopct='%1.0f%%')
plt.title("Répartition des météorites observées et découvertes")
# Save the plot as a PNG image
plot_dir = "plot"
plot_file_name = "08_meteorite_fall.png"
plt.savefig(f"{plot_dir}/{plot_file_name}")
print(f"Plot saved as {plot_dir}/{plot_file_name}")

# show the plot
plt.show()
input()
# Close the plot
plt.close()