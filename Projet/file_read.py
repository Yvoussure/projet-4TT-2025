import pandas as pd

df = pd.read_csv('steamdb.csv')

df2 = df[['Name', 'All-Time Peak']]
df2 = df2.sort_values(by='All-Time Peak', ascending=False)

df2['All-Time Peak'] = pd.to_numeric(df2['All-Time Peak'], errors='coerce')

df2['All-Time Peak'] = df2['All-Time Peak'].apply(lambda x: f"{int(x):,}" if pd.notnull(x) else x)

print(df2)