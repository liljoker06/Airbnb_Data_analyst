import seaborn as sns
import matplotlib.pyplot as plt

def visualiser_boxplot_avec_valeurs(df, colonne):
    """ Affiche un boxplot de la colonne spécifiée avec annotations optimisées. """

    # 🔹 Nettoyage : suppression des symboles "$" et conversion en float
    if colonne == 'price' and df['price'].dtype == 'object':
        print("🔄 Nettoyage des valeurs de la colonne price...")
        df = df.copy()  # Éviter de modifier le DataFrame original
        df['price'] = df['price'].str.replace('[\$,]', '', regex=True).astype(float)

    # 📊 Création du boxplot
    print("📊 Création du graphique boxplot...")
    plt.figure(figsize=(6, 8))
    ax = sns.boxplot(y=df[colonne])
    plt.title(f"Boxplot de la colonne {colonne}")

    # Calcul des valeurs des quartiles et des outliers
    Q1 = df[colonne].quantile(0.25)
    Q3 = df[colonne].quantile(0.75)
    median = df[colonne].median()
    IQR = Q3 - Q1
    outliers = df[(df[colonne] < (Q1 - 1.5 * IQR)) | (df[colonne] > (Q3 + 1.5 * IQR))]

    # Ajouter des annotations pour les quartiles
    ax.annotate(f'Q1: {Q1:.2f}', xy=(0, Q1), xytext=(-0.3, Q1),
                textcoords='offset points', ha='center', color='blue', fontsize=10)
    ax.annotate(f'Q3: {Q3:.2f}', xy=(0, Q3), xytext=(-0.3, Q3),
                textcoords='offset points', ha='center', color='blue', fontsize=10)
    ax.annotate(f'Médiane: {median:.2f}', xy=(0, median), xytext=(-0.3, median),
                textcoords='offset points', ha='center', color='blue', fontsize=10)

    # Affichage limité des outliers (max 10 pour éviter surcharge)
    for i, val in enumerate(outliers[colonne].head(10)):
        ax.annotate(f'{val:.2f}', xy=(0, val), xytext=(0.1, val),
                    textcoords='offset points', ha='left', color='red', fontsize=9)

    plt.show()