import pandas as pd

df = pd.read_csv("shopping_trends.csv")

with open("wshlecon.txt","w") as tktwsh:
    df_head_str = df.head().to_string()
    tktwsh.write(df_head_str)

print(df.tail(n = 10))

print(df.describe().T)

print(df.info(show_counts=True, memory_usage=True, verbose=True))