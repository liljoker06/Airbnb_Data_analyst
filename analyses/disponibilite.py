import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyse_disponibilite(df):
    print("🔍 Analyse des disponibilités en cours...\n")

    print("📋 Colonnes disponibles :", df.columns)

    # Vérifier si 'availability_365' existe
    if 'availability_365' not in df.columns:
        raise KeyError("⚠️ La colonne 'availability_365' est introuvable ! Vérifiez les colonnes disponibles.")

    # 🔹 Nettoyage : s'assurer que 'availability_365' est un entier (si nécessaire)
    if df['availability_365'].dtype != 'int64' and df['availability_365'].dtype != 'float64':
        print("🔄 Nettoyage des valeurs de la colonne 'availability_365'...")
        df['availability_365'] = pd.to_numeric(df['availability_365'], errors='coerce')

    # 🔹 Analyse de la disponibilité moyenne
    disponibilite_moyenne = df['availability_365'].mean().round(2)
    print(f"\n📅 Disponibilité moyenne des logements sur 365 jours : {disponibilite_moyenne} jours")

    # 🔹 Proportion des logements disponibles (ayant des jours de disponibilité > 0)
    proportion_disponibles = (df['availability_365'] > 0).mean() * 100
    print(f"\n📊 Proportion des logements disponibles : {proportion_disponibles:.2f}%")

    # 🔹 Logements les plus disponibles (les plus proches de 365 jours)
    logements_plus_disponibles = df[df['availability_365'] == 365].shape[0]
    print(f"\n🏡 Nombre de logements disponibles toute l'année (365 jours) : {logements_plus_disponibles}")

    # 🔹 Logements avec la plus grande disponibilité
    top_logements_disponibles = df.sort_values('availability_365', ascending=False).head(10)
    print("\n🚀 Top 10 des logements avec la plus grande disponibilité :")
    print(top_logements_disponibles[['name', 'neighbourhood', 'availability_365']])

    # 📊 Graphiques
    print("\n⚙️ Génération des graphiques... Cela peut prendre quelques secondes.")

    # Graphique 1: Distribution de la disponibilité (histogramme)
    print("📈 Création du graphique : Distribution de la disponibilité des logements...")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['availability_365'], bins=30, kde=True, color='skyblue', stat='density')
    plt.title('Distribution de la Disponibilité des Logements sur 365 jours')
    plt.xlabel('Jours de disponibilité')
    plt.ylabel('Densité')
    plt.grid(True)
    plt.show()

    # Graphique 2: Proportion des logements disponibles vs non disponibles (pie chart)
    print("🍰 Création du graphique : Proportion des logements disponibles vs non disponibles...")
    available_count = (df['availability_365'] > 0).sum()
    not_available_count = df.shape[0] - available_count
    plt.figure(figsize=(6, 6))
    plt.pie([available_count, not_available_count], labels=['Disponibles', 'Non Disponibles'], autopct='%1.1f%%',
            colors=['#66b3ff', '#ff6666'])
    plt.title('Proportion des Logements Disponibles vs Non Disponibles')
    plt.show()

    # Graphique 3: Top 10 des logements les plus disponibles (bar plot)
    print("📊 Création du graphique : Top 10 des logements avec la plus grande disponibilité...")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='availability_365', y='name', data=top_logements_disponibles, palette='viridis')
    plt.title('Top 10 des Logements avec la Plus Grande Disponibilité')
    plt.xlabel('Jours de disponibilité')
    plt.ylabel('Nom du logement')
    plt.show()