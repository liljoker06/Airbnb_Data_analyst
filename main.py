import pandas as pd
from analyses.quartier import analyse_quartier
from analyses.prix import analyse_prix
from analyses.disponibilite import analyse_disponibilite
from analyses.valeurs_aberrantes import visualiser_boxplot_avec_valeurs

# Charger le fichier Parquet
df = pd.read_parquet("./csv-data/airbnb_filtered.parquet")

# Execution les analystes
analyse_disponibilite(df)
analyse_prix(df)
analyse_quartier(df)

visualiser_boxplot_avec_valeurs(df, "price")