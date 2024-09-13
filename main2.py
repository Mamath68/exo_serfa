print("BIENVENUE AU JEU DU PENDU")

import random
import string
from liste_mots import mots

# print(mots)


def choix_mot_valide(mots):
    mot = random.choice(mots)  # choisit un mot au hasard
    while "-" in mot or " " in mot or "é" in mot:
        mot = random.choice(mots)  # on tire un autre mot au hasard
    return mot.upper()  # renvoie le mot valide en majuscules


# def pendu():
mot = choix_mot_valide(mots)
lettres_mot = set(mot)  # récupère dans un ensemble les lettres du mot (sans doublons)
alphabet = set(
    string.ascii_uppercase
)  # ensemble qui contient les lettres de l'alphabet en majuscules
lettres_util = set()  # ensemble vide qui stockera les lettres déjà proposées
# Limiter le nombre de tentatives
vies = 6

mot_cherche = [lettre if lettre in lettres_util else "_" for lettre in mot]

print("Le mot recherché est : ", " ".join(mot_cherche))

lettre_user = input("Saisissez une lettre svp :").upper()

if lettre_user in alphabet:
    lettres_util.add(lettre_user)
    if lettre_user in lettres_mot:
        lettres_mot.remove(lettre_user)
    else:
        vies = vies - 1
        print("Cette lettre n'est pas dans le mot. Vous perdez 1 vie")
        print("Il vous reste", vies, "vies")
else:
    print(
        "Ce caractère n'est pas une lettre de l'alphabet. veuillez renseigner une lettre"
    )
