# La classe Wizard a les attributs suivants :

# dégat : valeur aléatoire entre 2 et 4
# chance : valeur de 20
# fuite : valeur de 10
# prix : valeur de 15
# type d'unité : "wizard"
# Note : la fonction choice du module random peut vous aider,
#  e.g. random.choice(range(10)), random.choice(["ceci", "est", "un", "test"])

import random
class Wizard():
    chance = 20
    fuite = 10
    prix = 15
    

    def __init__(self) -> None:   
        self.degat = random.randint(2, 4)
        self.unite = "wizard"


