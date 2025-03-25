# 📌 Projet : Estimation du Prix d'un Logement Airbnb

## 🎯 Objectif
L'objectif de ce projet est de proposer **le prix optimal** d’un nouveau logement sur **Airbnb** en fonction des caractéristiques des biens existants. 

## 🏡 Problématique
> _Quelle est la meilleure estimation de prix à proposer pour un logement sur Airbnb ?_

## 📊 Méthodologie
Nous avons sélectionné les **colonnes les plus pertinentes** pour évaluer les logements Airbnb, en excluant les informations redondantes ou non essentielles afin de concentrer l'analyse sur les **facteurs influençant directement le prix et la décision de location**.

### 🗃️ Données utilisées
Les données utilisées proviennent de **[Inside Airbnb](https://insideairbnb.com/fr/get-the-data/)**. 

📂 **Organisation des fichiers** :
- Créez un dossier `csv-data` à la racine du projet.
- Téléchargez les fichiers CSV depuis [Inside Airbnb](https://insideairbnb.com/fr/get-the-data/).
- Placez-les dans le dossier `csv-data`.

Deux fichiers principaux sont utilisés :
- **`listings.csv`** : Contient les informations détaillées des logements.
- **`calendar.csv`** : Contient les disponibilités et variations de prix des logements au fil du temps.

### 📂 Structure du projet
```
📁 Airbnb_data_analyst/
│── 📁 csv-data/           # Contient les fichiers CSV et Parquet fusionnés
│   │── 📄 airbnb_filtered.parquet  # Fichier fusionné des données
│   │── 📄 calender.csv     # Données de disponibilité des logements
│   │── 📄 listings.csv     # Données des logements Airbnb
│
│── 📁 analyses/           # Contient les différents types d'analyses
│   │── 📄 prix.py         # Analyse des prix
│   │── 📄 disponibilite.py # Analyse de la disponibilité
│   │── 📄 quartier.py     # Analyse des quartiers
│   │── 📄 __init__.py      # Permet d'importer les analyses comme un package
│
│── 📄 fusion.py          # Script de fusion des données
│── 📄 main.py            # Point d'entrée du projet
│── 📄 requirements.txt    # Dépendances du projet
│── 📄 README.md          # Documentation du projet
│── 📁 venv/              # Environnement virtuel Python
```

### 🔍 Sélection des variables clés
Nous avons retenu les colonnes suivantes :
#### 🔹 `listings.csv`
- `id` : Identifiant unique du logement
- `name` : Nom du logement
- `host_id` : Identifiant du propriétaire
- `host_name` : Nom du propriétaire
- `neighbourhood` : Quartier du logement
- `latitude`, `longitude` : Localisation géographique
- `room_type` : Type de logement (chambre privée, logement entier, etc.)
- `price` : Prix actuel du logement
- `minimum_nights` : Nombre minimum de nuits requises
- `number_of_reviews` : Nombre total d’avis
- `availability_365` : Disponibilité sur l'année

#### 🔹 `calendar.csv`
- `listing_id` : Référence au logement
- `date` : Date de disponibilité
- `available` : Indique si le logement est disponible ou non
- `price` : Prix ajusté par jour

### 🛠️ Traitement des Données
1. **Filtrage des colonnes pertinentes** pour l'analyse.
2. **Fusion des fichiers** pour obtenir un seul jeu de données combinant caractéristiques des logements et informations sur les prix.
3. **Suppression des valeurs nulles et des doublons** pour assurer la fiabilité des résultats.
4. **Analyse statistique et visualisation** des données pour identifier les facteurs influençant les prix.

### 📈 Analyses effectuées
Le projet inclut plusieurs analyses :
- **Analyse des prix (`prix.py`)** : Calcul du prix moyen par type de logement et par quartier.
- **Analyse de la disponibilité (`disponibilite.py`)** : Étude des tendances de disponibilité et taux d’occupation.
- **Analyse des quartiers (`quartier.py`)** : Comparaison des quartiers les plus chers et les plus prisés.

## 🚀 Exécution du Projet
1. **Création de l'environnement virtuel** :
   ```sh
   python -m venv venv
   ```
2. **Activation de l'environnement virtuel** :
   ```sh
   # Sous Windows
   venv\Scripts\activate
   
   # Sous macOS/Linux
   source venv/bin/activate
   ```
3. **Installation des dépendances** :
   ```sh
   pip install -r requirements.txt
   ```
4. **Exécution du script de fusion des données** :
   ```sh
   python fusion.py
   ```
5. **Exécution des analyses via `main.py`** :
   ```sh
   python main.py
   ```

## 📌 Résultats Attendus
- Une meilleure compréhension des **facteurs qui influencent le prix** d’un logement Airbnb.
- Une **analyse approfondie de la disponibilité et des tendances des quartiers**.
- Un modèle permettant de **prédire le prix optimal** pour un nouveau bien.

