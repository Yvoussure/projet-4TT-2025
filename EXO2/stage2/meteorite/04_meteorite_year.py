import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

# Afficher le nombre de météorites tombés par année
print(f"Nombre de météorites tombées par année :")
print(df['year'].value_counts().sort_index())

# Afficher les 10 années avec le plus de météorites tombées triées par ordre croissant
print(f"\nLes 10 années avec le plus de météorites tombées :")
print(df['year'].value_counts().sort_values(ascending=False).head(10))