import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def afficher_colonnes(df):
    """Affiche les colonnes disponibles dans le DataFrame."""
    print("📋 Colonnes disponibles :", df.columns)


def nettoyer_colonne_disponibilite(df):
    """Nettoie la colonne 'availability_365' pour s'assurer qu'elle est numérique."""
    if 'availability_365' not in df.columns:
        raise KeyError("⚠️ La colonne 'availability_365' est introuvable ! Vérifiez les colonnes disponibles.")

    if df['availability_365'].dtype != 'int64' and df['availability_365'].dtype != 'float64':
        print("🔄 Nettoyage des valeurs de la colonne 'availability_365'...")
        df['availability_365'] = pd.to_numeric(df['availability_365'], errors='coerce')
    return df


def afficher_disponibilite_moyenne(df):
    """Affiche la disponibilité moyenne des logements sur 365 jours."""
    disponibilite_moyenne = df['availability_365'].mean().round(2)
    print(f"\n📅 Disponibilité moyenne des logements sur 365 jours : {disponibilite_moyenne} jours")
    return disponibilite_moyenne


def afficher_proportion_disponibles(df):
    """Affiche la proportion de logements disponibles (ayant des jours de disponibilité > 0)."""
    proportion_disponibles = (df['availability_365'] > 0).mean() * 100
    print(f"\n📊 Proportion des logements disponibles : {proportion_disponibles:.2f}%")
    return proportion_disponibles


def afficher_logements_plus_disponibles(df):
    """Affiche le nombre de logements disponibles toute l'année (365 jours)."""
    logements_plus_disponibles = df[df['availability_365'] == 365].shape[0]
    print(f"\n🏡 Nombre de logements disponibles toute l'année (365 jours) : {logements_plus_disponibles}")
    return logements_plus_disponibles


def afficher_top_logements_disponibles(df):
    """Affiche le top 10 des logements avec la plus grande disponibilité."""
    top_logements_disponibles = df.sort_values('availability_365', ascending=False).head(10)
    print("\n🚀 Top 10 des logements avec la plus grande disponibilité :")
    print(top_logements_disponibles[['name', 'neighbourhood', 'availability_365']])
    return top_logements_disponibles


def graphe_distribution_disponibilite(df):
    """Affiche un graphique de la distribution de la disponibilité des logements."""
    print("📈 Création du graphique : Distribution de la disponibilité des logements...")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['availability_365'], bins=30, kde=True, color='skyblue', stat='density')
    plt.title('Distribution de la Disponibilité des Logements sur 365 jours')
    plt.xlabel('Jours de disponibilité')
    plt.ylabel('Densité')
    plt.grid(True)
    plt.show()


def graphe_proportion_disponibles(df):
    """Affiche un graphique de la proportion des logements disponibles vs non disponibles."""
    print("🍰 Création du graphique : Proportion des logements disponibles vs non disponibles...")
    available_count = (df['availability_365'] > 0).sum()
    not_available_count = df.shape[0] - available_count
    plt.figure(figsize=(6, 6))
    plt.pie([available_count, not_available_count], labels=['Disponibles', 'Non Disponibles'], autopct='%1.1f%%',
            colors=['#66b3ff', '#ff6666'])
    plt.title('Proportion des Logements Disponibles vs Non Disponibles')
    plt.show()


def graphe_top_logements_disponibles(top_logements_disponibles):
    """Affiche un graphique du top 10 des logements les plus disponibles."""
    print("📊 Création du graphique : Top 10 des logements avec la plus grande disponibilité...")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='availability_365', y='name', data=top_logements_disponibles, palette='viridis')
    plt.title('Top 10 des Logements avec la Plus Grande Disponibilité')
    plt.xlabel('Jours de disponibilité')
    plt.ylabel('Nom du logement')
    plt.show()


def analyse_disponibilite(df):
    """Effectue une analyse complète de la disponibilité des logements."""
    print("🔍 Analyse des disponibilités en cours...\n")

    # Afficher les colonnes disponibles
    afficher_colonnes(df)

    # Nettoyer la colonne 'availability_365'
    df = nettoyer_colonne_disponibilite(df)

    # Afficher la disponibilité moyenne
    afficher_disponibilite_moyenne(df)

    # Afficher la proportion des logements disponibles
    afficher_proportion_disponibles(df)

    # Afficher le nombre de logements disponibles toute l'année
    afficher_logements_plus_disponibles(df)

    # Afficher le top 10 des logements les plus disponibles
    top_logements_disponibles = afficher_top_logements_disponibles(df)

    # Générer les graphiques
    print("\n⚙️ Génération des graphiques... Cela peut prendre quelques secondes.")
    graphe_distribution_disponibilite(df)
    graphe_proportion_disponibles(df)
    graphe_top_logements_disponibles(top_logements_disponibles)