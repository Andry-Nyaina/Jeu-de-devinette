# jeu.py

import random
import time
import json
from pathlib import Path

class JeuDevinette:
    def __init__(self, min_val=1, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.nombre_secret = random.randint(min_val, max_val)
        self.essais = 0
        self.start_time = None

    def jouer(self):
        print(f"Devinez le nombre entre {self.min_val} et {self.max_val} !")
        self.start_time = time.time()

        while True:
            try:
                choix = int(input("Votre choix : "))
                self.essais += 1

                if choix < self.nombre_secret:
                    print("Trop petit.")
                elif choix > self.nombre_secret:
                    print("Trop grand.")
                else:
                    duree = round(time.time() - self.start_time, 2)
                    print(f"Bravo ! Vous avez trouvé en {self.essais} essais et {duree} secondes.")
                    return self.essais, duree
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def enregistrer_score(self, pseudo, essais, duree, fichier="scores.json"):
        score = {"pseudo": pseudo, "essais": essais, "temps": duree}
        path = Path(fichier)
        if path.exists():
            with path.open("r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(score)
        with path.open("w") as f:
            json.dump(data, f, indent=4)

    def afficher_scores(self, fichier="scores.json"):
        path = Path(fichier)
        if path.exists():
            with path.open("r") as f:
                data = json.load(f)
                print("\n--- Scores précédents ---")
                for score in data:
                    print(f"{score['pseudo']} - {score['essais']} essais - {score['temps']}s")
        else:
            print("Aucun score enregistré.")
