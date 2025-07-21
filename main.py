# main.py

from jeu import JeuDevinette

def main():
    """Programme principal pour lancer le jeu de devinette et gérer les scores
    """
    print("Bienvenue dans le jeu de devinette !")
    pseudo = input("Entrez votre nom : ")

    jeu = JeuDevinette()
    essais, duree = jeu.jouer()

    jeu.enregistrer_score(pseudo, essais, duree)

    voir = input("Voulez-vous voir les scores ? (o/n) : ").lower()
    if voir == 'o':
        jeu.afficher_scores()

if __name__ == "__main__":
    main()
