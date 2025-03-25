import pandas as pd 
import analyses.prix as analyse_prix





# Charger le fichier Parquet
df = pd.read_parquet("./csv-data/airbnb_filtered.parquet")


# Execution les analystes 
analyse_prix.analyse_prix(df)

