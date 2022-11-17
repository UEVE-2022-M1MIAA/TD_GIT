# a classe Orc a les attributs suivants :

# dégat : valeur aléatoire entre 3 et 5
# loot: valeur aléatoire entre 2 et 2.5
# Note : la fonction choice du module random peut vous aider, e.g. 
# random.choice(range(10)), random.choice(["ceci", "est", "un", "test"])

import random
class Orc():
    

    def __init__(self) -> None:   
        self.degat =random.randint(3, 5)
        self.loot = random.uniform(2, 2.5)


