import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

print({f"Nombre de méteorites{len(df)}"})