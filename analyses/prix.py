import pandas as pd 

def analyse_prix(df):
    print("🔍 Analyse des prix en cours...\n")

    print("📋 Colonnes disponibles :", df.columns)

    # Vérifier si 'price' existe
    if 'price' not in df.columns:
        raise KeyError("⚠️ La colonne 'price' est introuvable après la fusion ! Vérifiez les colonnes disponibles.")

    # 🔹 Nettoyage : suppression des symboles "$" et conversion en float
    if df['price'].dtype == 'object':  
        print("🔄 Nettoyage des valeurs de la colonne price...")
        df['price'] = df['price'].str.replace('[\$,]', '', regex=True).astype(float)

    # Prix moyen par type de logement, arrondi à 2 décimales et formaté en €
    prix_par_type = df.groupby('room_type')['price'].mean().round(2).astype(str) + " €"
    print("\n🏠 Prix moyen par type de logement :")
    print(prix_par_type)

    # Quartiers les plus chers, arrondi à 2 décimales et formaté en €
    quartiers_chers = df.groupby('neighbourhood')['price'].mean().round(2).sort_values(ascending=False).astype(str) + " €"
    print("\n🏙️ Quartiers les plus chers :")
    print(quartiers_chers)
