import pandas as pd

df = pd.read_csv('Meteorite_Landings.csv')

df2 = df['mass (g)']
df3 = df['mass (g)'].mean()
print(df2,"La masse moyen est", df3)