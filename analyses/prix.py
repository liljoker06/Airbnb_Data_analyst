import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Prix moyen par type de logement
    prix_par_type = df.groupby('room_type')['price'].mean().round(2)
    print("\n🏠 Prix moyen par type de logement :")
    print(prix_par_type)

    # Quartiers les plus chers
    quartiers_chers = df.groupby('neighbourhood')['price'].mean().round(2).sort_values(ascending=False)
    print("\n🏙️ Quartiers les plus chers :")
    print(quartiers_chers)

    # 🔍 Visualisation des prix moyens par type de logement
    plt.figure(figsize=(8, 6))
    sns.barplot(x=prix_par_type.index, y=prix_par_type.values, palette="viridis")
    plt.title("Prix moyen par type de logement", fontsize=16)
    plt.xlabel("Type de logement", fontsize=12)
    plt.ylabel("Prix moyen (€)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 🔍 Visualisation des quartiers les plus chers (top 10)
    top_quartiers = quartiers_chers.head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_quartiers.values, y=top_quartiers.index, palette="magma")
    plt.title("Top 10 des quartiers les plus chers", fontsize=16)
    plt.xlabel("Prix moyen (€)", fontsize=12)
    plt.ylabel("Quartier", fontsize=12)
    plt.tight_layout()
    plt.show()