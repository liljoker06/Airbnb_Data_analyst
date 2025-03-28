import pandas as pd

# Charger le fichier Parquet
df = pd.read_parquet("./csv-data/airbnb_filtered.parquet")


print(df.head())


print(df.shape)

print(df.shape)

print(df.dtypes)

