import os
import pandas as pd
import dask.dataframe as dd  


data_folder = "./csv-data"
listing_file = os.path.join(data_folder, "listings.csv")
calendar_file = os.path.join(data_folder, "calender.csv")  # Vérifie l'orthographe !
output_file = os.path.join(data_folder, "airbnb_filtered.parquet")  # Format rapide


if not os.path.exists(listing_file):
    print(f"❌ Erreur : Le fichier {listing_file} est introuvable.")
    exit()
if not os.path.exists(calendar_file):
    print(f"❌ Erreur : Le fichier {calendar_file} est introuvable.")
    exit()


listings_cols = [
    "id", "name", "host_id", "host_name", "neighbourhood", "latitude", "longitude",
    "room_type", "price", "minimum_nights", "number_of_reviews", "availability_365"
]
calendar_cols = ["listing_id", "date", "available", "price"]


print("📖 Lecture et nettoyage du fichier listings.csv...")
listings_df = pd.read_csv(listing_file, usecols=listings_cols)
listings_df.drop_duplicates(subset=["id"], inplace=True)  # Supprime les doublons
print(f"✔️ {len(listings_df):,} lignes uniques chargées depuis listings.csv.")

print("📖 Lecture et traitement du fichier calendar.csv en parallèle...")
calendar_df = dd.read_csv(calendar_file, usecols=calendar_cols, blocksize="500MB")  # Lecture par blocs

calendar_df = calendar_df.compute()  # Transformation complète en Pandas
calendar_df.drop_duplicates(subset=["listing_id", "date"], inplace=True)  # Supprime les doublons

print("🔄 Fusion des fichiers...")
merged_df = listings_df.merge(calendar_df, left_on="id", right_on="listing_id", how="inner")
merged_df.drop(columns=["listing_id"], inplace=True)  # Nettoyage

# 📌 Garder uniquement le prix du calendrier et renommer proprement
if "price_x" in merged_df.columns and "price_y" in merged_df.columns:
    merged_df.drop(columns=["price_x"], inplace=True)  # Supprime price_x (listing.csv)
    merged_df.rename(columns={"price_y": "price"}, inplace=True)  # Renomme price_y en price

merged_df.drop_duplicates(inplace=True)  # Supprime les doublons

print(f"💾 Sauvegarde du fichier fusionné dans {output_file}...")
merged_df.to_parquet(output_file, index=False, engine="fastparquet")

print("✅ Fusion terminée avec succès !")

