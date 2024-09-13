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
