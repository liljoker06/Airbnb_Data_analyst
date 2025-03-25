import pandas as pd

def analyse_quartier(df):
    print("🔍 Analyse des quartiers en cours...\n")

    # print("📋 Colonnes disponibles :", df.columns)

    # Vérifier les colonnes
    if 'neighbourhood' not in df.columns:
        raise KeyError("⚠️ La colonne 'neighbourhood' est introuvable après la fusion !")
    if 'price' not in df.columns:
        raise KeyError("⚠️ La colonne 'price' est introuvable après la fusion !")

    # Nettoyage éventuel
    if df['price'].dtype == 'object':  
        print("🔄 Nettoyage des valeurs de la colonne price...")
        df['price'] = df['price'].str.replace('[\$,]', '', regex=True).astype(float)

    # Prix moyen par quartier
    prix_par_quartier = df.groupby('neighbourhood')['price'].mean().round(2).sort_values(ascending=False)
    print("\n💶 Prix moyen par quartier :")
    print(prix_par_quartier.astype(str) + " €")

    # Nombre total de logements par quartier
    nb_logements_par_quartier = df['neighbourhood'].value_counts()
    print("\n🏘️ Nombre total de logements par quartier :")
    print(nb_logements_par_quartier)

    # Top 5 des quartiers les plus chers
    quartiers_chers = prix_par_quartier.head(5)
    print("\n💎 Top 5 des quartiers les plus chers :")
    print(quartiers_chers.astype(str) + " €")

    # Top 5 des quartiers les plus prisés
    quartiers_prises = nb_logements_par_quartier.head(5)
    print("\n🔥 Top 5 des quartiers les plus prisés (en nombre d’annonces) :")
    print(quartiers_prises)
