# Projet d'Analyse ADN
## Analyse des Séquences Génétiques et Visualisation des Mutations

### 📖 Description du Projet

Ce projet implémente un système complet d'analyse d'ADN permettant l'étude des séquences génétiques, la détection de mutations et la visualisation graphique des données. Le programme traite des séquences d'ADN, identifie les différents types de mutations (substitutions, insertions, délétions) et génère des graphiques statistiques détaillés.

### ✨ Fonctionnalités Principales

- **Analyse de séquences ADN** : Lecture et traitement de fichiers FASTA
- **Détection de mutations** : Identification automatique des variations génétiques
- **Visualisation graphique** : Graphiques statistiques avec matplotlib
- **Rapport détaillé** : Génération automatique de rapports d'analyse
- **Interface utilisateur** : Interface graphique intuitive avec Tkinter

### 🛠️ Prérequis

- Python 3.7 ou supérieur
- Les bibliothèques Python suivantes :
  ```
  matplotlib
  tkinter
  ```

### 📦 Installation

1. **Cloner le projet :**
   ```bash
   git clone <repository-url>
   cd DNA
   ```

2. **Installer les dépendances :**
   ```bash
   pip install matplotlib
   # tkinter est généralement inclus avec Python
   ```

3. **Vérifier l'installation :**
   ```bash
   python -c "import matplotlib, tkinter; print('Dépendances installées avec succès')"
   ```

### 🚀 Utilisation

#### Méthode 1 : Interface Graphique
```bash
python interface_adn.py
```

#### Méthode 2 : Ligne de Commande
```bash
python main.py
```

#### Exemples d'Utilisation

1. **Charger une séquence ADN :**
   - Placer le fichier `sequence.txt` dans le dossier du projet
   - Lancer l'interface graphique
   - Cliquer sur "Charger Séquence"

2. **Analyser les mutations :**
   - Charger une séquence de référence et une séquence mutée
   - Cliquer sur "Analyser Mutations"
   - Consulter les résultats dans la zone de texte

3. **Générer des graphiques :**
   - Après l'analyse, cliquer sur "Générer Graphiques"
   - Les graphiques s'affichent automatiquement

### 📁 Structure du Projet

```
DNA/
├── main.py              # Module backend - logique d'analyse
├── interface_adn.py     # Interface graphique Tkinter
├── sequence.txt         # Fichier exemple de séquence ADN
├── rapport.md           # Rapport détaillé du projet
├── README.md            # Ce fichier
├── .env.example         # Exemple de configuration
└── .gitignore           # Fichiers à exclure de Git
```

### 📊 Format des Données

Les séquences ADN doivent être au format texte simple :
```
ATCGATCGATCGATCG...
```

Ou au format FASTA :
```
>Sequence_1
ATCGATCGATCGATCG
TACGATCGATCGATCG
```

### 🔧 Configuration

1. **Copier le fichier de configuration :**
   ```bash
   cp .env.example .env
   ```

2. **Modifier les paramètres si nécessaire :**
   ```bash
   # Aucune configuration spéciale requise pour ce projet
   ```

### 📈 Exemples de Résultats

Le programme génère plusieurs types d'analyses :

- **Composition nucléotidique** : Pourcentages de A, T, C, G
- **Détection de mutations** : Substitutions, insertions, délétions
- **Graphiques statistiques** : Histogrammes et diagrammes
- **Rapport détaillé** : Analyse complète au format markdown

### 🔍 Fonctionnalités Détaillées

#### Analyse des Séquences
- Validation des séquences ADN
- Calcul de la composition en bases
- Détection des motifs répétés

#### Détection de Mutations
- Comparaison de séquences
- Classification des mutations
- Localisation précise des variations

#### Visualisation
- Graphiques en barres de composition
- Histogrammes de mutations
- Diagrammes statistiques

### 🐛 Dépannage

**Problème : Matplotlib ne s'affiche pas**
```bash
# Sur macOS avec Anaconda
conda install python.app
# Ou utiliser un backend différent
export MPLBACKEND=TkAgg
```

### 📝 Notes

- Les fichiers de séquences doivent être encodés en UTF-8
- Les séquences peuvent contenir des caractères IUPAC standard
- Le programme gère automatiquement les séquences en majuscules/minuscules

### 🤝 Contribution

Pour contribuer au projet :
1. Fork le repository
2. Créer une branche feature
3. Commit les changements
4. Créer une Pull Request

### 📄 Licence

Ce projet est à des fins éducatives dans le cadre du cursus ECE.

### 📞 Contact

Pour toute question concernant ce projet, veuillez consulter la documentation ou créer une issue sur GitHub.

---

**Développé dans le cadre du projet ECE B3 - Analyse ADN**