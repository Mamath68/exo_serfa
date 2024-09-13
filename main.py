from liste_mots import mots
import random
import string

mot = random.choice(mots)

# mot = "ELEPHANT"
while mot == "-" or mot == " ":
    mot = random.choice(mots)

hide = "_" * len(mot)

print(mot)
print(hide)
