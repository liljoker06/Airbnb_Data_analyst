import pandas as pd 
import analyses.prix as analyse_prix
import analyses.quartier as analyse_quartier
from analyses.disponibilite import analyse_disponibilite

# Charger le fichier Parquet
df = pd.read_parquet("./csv-data/airbnb_filtered.parquet")


# Execution les analystes 
analyse_disponibilite(df)
analyse_prix.analyse_prix(df)
analyse_quartier.analyse_quartier(df)

