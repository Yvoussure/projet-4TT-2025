import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

# Afficher le nombre de météorites tombés par classe
print(f"Nombre de météorites tombées par classe :")
print(df['recclass'].value_counts().sort_index())

# Afficher les 10 classes avec le plus de météorites tombées triées par ordre croissant
print(f"\nLes 10 classes avec le plus de météorites tombées :")
print(df['recclass'].value_counts().sort_values(ascending=False).head(10))