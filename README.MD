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

### 📈 Modèle de Prédiction
Une fois les données nettoyées et consolidées, nous appliquerons des modèles de **Machine Learning** pour prédire le prix optimal d'un logement en fonction de ses caractéristiques.

## 🚀 Exécution du Projet
1. **Installation des dépendances** :
   ```sh
   pip install -r requirements.txt
   ```
2. **Exécution du script de fusion des données** :
   ```sh
   python fusion.py
   ```
3. **Exploration et analyse des données** :
   ```sh
   python analyse.py
   ```

## 📌 Résultats Attendus
- Une meilleure compréhension des **facteurs qui influencent le prix** d’un logement Airbnb.
- Un modèle permettant de **prédire le prix optimal** pour un nouveau bien.



