import pandas as pd
import msvcrt
df = pd.read_csv("dataset.csv", index_col="id")
print(df)

print(df.describe())
print(df.head())
print(df.tail())


msvcrt.getch()