import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

# Afficher le nombre de météorites en-dessous de la masse médiane
print(f"Nombre de météorites en-dessous de la masse médiane : {df[df['mass (g)'] < df['mass (g)'].median()]['mass (g)'].count()}")