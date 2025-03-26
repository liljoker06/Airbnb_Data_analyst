import seaborn as sns
import matplotlib.pyplot as plt

def visualiser_boxplot_avec_valeurs(df, colonne):
    # 🔹 Nettoyage : suppression des symboles "$" et conversion en float
    if colonne == 'price':
        if df['price'].dtype == 'object':
            print("🔄 Nettoyage des valeurs de la colonne price...")
            df['price'] = df['price'].str.replace('[\$,]', '', regex=True).astype(float)

    # 📊 Création du boxplot vertical
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

    # Ajouter des annotations pour les quartiles (version verticale)
    ax.text(Q1, 0.05, f'Q1: {Q1:.2f}', horizontalalignment='center', verticalalignment='bottom', color='blue')
    ax.text(Q3, 0.05, f'Q3: {Q3:.2f}', horizontalalignment='center', verticalalignment='bottom', color='blue')
    ax.text(median, 0.05, f'Médiane: {median:.2f}', horizontalalignment='center', verticalalignment='bottom', color='blue')

    # Afficher les valeurs aberrantes (outliers) verticalement
    for i in outliers[colonne]:
        ax.text(i, 0.05, f'{i:.2f}', horizontalalignment='center', verticalalignment='bottom', color='red')

    plt.show()