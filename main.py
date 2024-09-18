from liste_mots import mots
import random
import string

# print(mots)

print("BIENVENUE AU JEU DU PENDU")


def choix_mot_valide(mots):
    mot = random.choice(mots)  # choisit un mot au hasard
    while "-" in mot or " " in mot or "é" in mot:  # évite les mots avec des espaces ou tirets
        mot = random.choice(mots)
    return mot.upper()


def pendu():
    mot = choix_mot_valide(mots)
    lettres_mot = set(mot)  # récupère dans un ensemble les lettres du mot (sans doublons)
    alphabet = set(string.ascii_uppercase)  # lettres de l'alphabet
    lettres_util = set()  # stockera les lettres déjà proposées
    vies = 6

    # Tant qu'il reste des vies et qu'il reste des lettres à deviner
    while len(lettres_mot) > 0 and vies > 0:
        # Afficher le mot actuel avec les lettres trouvées et des "_" pour les lettres manquantes
        mot_cherche = [lettre if lettre in lettres_util else "_" for lettre in mot]

        print("\nLe mot recherché est : ", " ".join(mot_cherche))
        print("Lettres déjà proposées : ", " ".join(lettres_util))

        # Saisie de l'utilisateur
        lettre_user = input("Saisissez une lettre : ").upper()

        # Vérification si la lettre est dans l'alphabet et n'a pas encore été proposée
        if lettre_user in alphabet - lettres_util:
            lettres_util.add(lettre_user)  # ajoute la lettre à l'ensemble des lettres proposées
            if lettre_user in lettres_mot:
                lettres_mot.remove(lettre_user)  # retire la lettre correcte des lettres à deviner
                print("Bonne lettre !")
            else:
                vies -= 1
                print(f"Cette lettre n'est pas dans le mot. Vous perdez une vie. Il vous reste {vies} vies.")
        # Si la lettre a déjà été proposée
        elif lettre_user in lettres_util:
            print("Vous avez déjà proposé cette lettre. Essayez-en une autre.")
        else:
            print("Ce n'est pas une lettre valide. Veuillez entrer une lettre de l'alphabet.")

# Fin du jeu
    if vies == 0:
        print(f"Vous avez perdu ! Le mot était : {mot}")
    else:
        print(f"Félicitations ! Vous avez trouvé le mot : {mot}")
pendu()