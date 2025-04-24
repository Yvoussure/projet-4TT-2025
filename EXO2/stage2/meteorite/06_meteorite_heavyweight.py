import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

# Afficher le nombre de météorites dépassant la masse moyenne
print(f"Nombre de météorites dépassant la masse moyenne : {df[df['mass (g)'] > df['mass (g)'].mean()]['mass (g)'].count()}")