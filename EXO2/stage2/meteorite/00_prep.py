import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

with open("describe.txt","w") as file1:
    df2 = df.describe().T.to_string()
    file1.write(df2)

with open("head.txt","w") as file2:
    df_head_str = df.head().to_string()
    file2.write(df_head_str)

with open("fall.txt","w") as file3:
    df3 = df[['name','fall']].to_string()
    file3.write(df3)

with open("recclass.txt","w") as file4:
    df4 = df[['name','recclass']].to_string()
    file4.write(df4)