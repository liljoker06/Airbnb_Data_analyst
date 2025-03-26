import pandas as pd

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
