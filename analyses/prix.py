import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def afficher_colonnes(df):
    """Affiche les colonnes disponibles dans le DataFrame."""
    print("📋 Colonnes disponibles :", df.columns)

def nettoyer_colonne_prix(df):
    """Nettoie la colonne 'price' en supprimant les symboles '$' et en la convertissant en float."""
    if 'price' not in df.columns:
        raise KeyError("⚠️ La colonne 'price' est introuvable après la fusion ! Vérifiez les colonnes disponibles.")
    
    if df['price'].dtype == 'object':
        print("🔄 Nettoyage des valeurs de la colonne price...")
        df['price'] = df['price'].str.replace('[\$,]', '', regex=True).astype(float)
    return df

def afficher_prix_par_type(df):
    """Affiche les prix moyens par type de logement avec la devise €."""
    prix_par_type = df.groupby('room_type')['price'].mean().round(2)
    print("\n🏠 Prix moyen par type de logement :")
    for room_type, price in prix_par_type.items():
        print(f"  - {room_type}: {price} €")
    return prix_par_type

def afficher_quartiers_chers(df):
    """Affiche les quartiers les plus chers avec la devise €."""
    quartiers_chers = df.groupby('neighbourhood')['price'].mean().round(2).sort_values(ascending=False)
    print("\n🏙️ Quartiers les plus chers :")
    for quartier, price in quartiers_chers.items():
        print(f"  - {quartier}: {price} €")
    return quartiers_chers

def graphe_prix_par_type(prix_par_type):
    """Affiche un graphique des prix moyens par type de logement."""
    plt.figure(figsize=(8, 6))
    sns.barplot(x=prix_par_type.index, y=prix_par_type.values, palette="viridis")
    plt.title("Prix moyen par type de logement", fontsize=16)
    plt.xlabel("Type de logement", fontsize=12)
    plt.ylabel("Prix moyen (€)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphe_quartiers_chers(quartiers_chers):
    """Affiche un graphique des 10 quartiers les plus chers."""
    top_quartiers = quartiers_chers.head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_quartiers.values, y=top_quartiers.index, palette="magma")
    plt.title("Top 10 des quartiers les plus chers", fontsize=16)
    plt.xlabel("Prix moyen (€)", fontsize=12)
    plt.ylabel("Quartier", fontsize=12)
    plt.tight_layout()
    plt.show()

def analyse_prix(df):
    print("🔍 Analyse des prix en cours...\n")
    
    # Afficher les colonnes disponibles
    afficher_colonnes(df)
    
    # Nettoyer la colonne 'price'
    df = nettoyer_colonne_prix(df)
    
    # Afficher les prix moyens par type de logement
    prix_par_type = afficher_prix_par_type(df)
    
    # Afficher les quartiers les plus chers
    quartiers_chers = afficher_quartiers_chers(df)
    
    # Générer les graphiques
    print("\n📊 Génération des graphiques...")
    graphe_prix_par_type(prix_par_type)
    graphe_quartiers_chers(quartiers_chers)