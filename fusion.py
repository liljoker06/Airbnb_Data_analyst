import os
import pandas as pd
import dask.dataframe as dd  

# 📂 Définition des chemins des fichiers
data_folder = "./csv-data"
listing_file = os.path.join(data_folder, "listings.csv")
calendar_file = os.path.join(data_folder, "calender.csv")  # Vérifie l'orthographe !
output_file = os.path.join(data_folder, "airbnb_filtered.parquet")  # Format rapide

# ✅ Vérification des fichiers
if not os.path.exists(listing_file):
    print(f"❌ Erreur : Le fichier {listing_file} est introuvable.")
    exit()
if not os.path.exists(calendar_file):
    print(f"❌ Erreur : Le fichier {calendar_file} est introuvable.")
    exit()

# 📌 Colonnes importantes
listings_cols = [
    "id", "name", "host_id", "host_name", "neighbourhood", "latitude", "longitude",
    "room_type", "price", "minimum_nights", "number_of_reviews", "availability_365"
]
calendar_cols = ["listing_id", "date", "available", "price"]

# 🔥 Lecture rapide du fichier listings.csv
print("📖 Lecture et nettoyage du fichier listings.csv...")
listings_df = pd.read_csv(listing_file, usecols=listings_cols)
listings_df.drop_duplicates(subset=["id"], inplace=True)  # Supprime les doublons
print(f"✔️ {len(listings_df):,} lignes uniques chargées depuis listings.csv.")

# 🔥 Lecture rapide de calendar.csv en mode Dask (optimisation mémoire)
print("📖 Lecture et traitement du fichier calendar.csv en parallèle...")
calendar_df = dd.read_csv(calendar_file, usecols=calendar_cols, blocksize="500MB")  # Lecture par blocs

# ✅ Convertir calendar_df en Pandas AVANT la fusion
calendar_df = calendar_df.compute()  # Transformation complète en Pandas
calendar_df.drop_duplicates(subset=["listing_id", "date"], inplace=True)  # Supprime les doublons

# 🔄 Fusion rapide avec pandas (maintenant que tout est en Pandas)
print("🔄 Fusion des fichiers...")
merged_df = listings_df.merge(calendar_df, left_on="id", right_on="listing_id", how="inner")
merged_df.drop(columns=["listing_id"], inplace=True)  # Nettoyage
merged_df.drop_duplicates(inplace=True)

# 💾 Sauvegarde ultra-rapide en Parquet (format optimisé)
print(f"💾 Sauvegarde du fichier fusionné dans {output_file}...")
merged_df.to_parquet(output_file, index=False, engine="fastparquet")

print("✅ Fusion terminée avec succès !")
