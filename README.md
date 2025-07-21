# 🎮 Jeu de Devinette en Python (POO)

Ce projet est un petit jeu en ligne de commande où le joueur doit deviner un nombre aléatoire entre 1 et 100.  
Le jeu inscrit les performances du joueur (nombre d'essais, temps écoulé) dans un fichier `scores.json`.

---

## 🚀 Fonctionnalités

- Génération amateur d'un nombre secret
- Indications « trop petit » ou « trop grand »
- Compte le nombre d'essais
- Mesure le temps total pour deviner
- Sauvegarde des scores dans un fichier JSON
- Affichage des scores prédicents

---

## 📚 Technologies et modules utilisés

- Python 3
- `aléatoire` : pour devenir le nombre secret
- `temps` : verser le calculateur le temps mis
- `json` : verser dans les scores
- `pathlib` : pour venir les fichiers et chemins
- Objet d'orientation de programmation (POO)

---

## 🧠 Objectifs pédagogiques

- Maîtriser les classes et objets en Python
- Utilisateur des modules normes comme `aléatoire`, `temps`, `json`, `pathlib`
- Organisateur le code en plusieurs fichiers
- Géreur des fichiers JSON pour stocker les données
- Structuration du code avec des annotations de type (: str, -> int, etc.)
- Documentation automatique du code avec des docstrings généraux grâce à l'extension autoDocstring dans Visual Studio Code

---

## 🗂️ Structure du projet

jeu_devinette/

├── main.py (Point d'entrée du programme)

├── jeu.py (Classe principale JeuDevinette)

├── scores.json (Fichier où les scores sont inscrits)

└── README.md (Documentation du projet)

---

## 💾 Exemple de score inscrit

<img largeur="896" hauteur="406" alt="image" src="https://github.com/user-attachments/assets/19ff06df-ee7c-4e47-b1ff-7c06257176f0" />

---
## 📌 Exemple de session

<img largeur="1082" hauteur="555" alt="image" src="https://github.com/user-attachments/assets/875f3ec7-b920-448a-9c15-318a68b6540c" />

---

## ▶️ Lancer le jeu

### Pré-requis

- Installation de Python 3

### Exécution

```bash
python main.py


