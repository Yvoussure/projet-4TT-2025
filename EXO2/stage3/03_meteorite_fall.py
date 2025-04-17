import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

print(f"Nombre de météorites tombées : {df[df['fall'] == 'Fell']['fall'].count()}")
print(f"Nombre de météorites observées : {df[df['fall'] == 'Found']['fall'].count()}")