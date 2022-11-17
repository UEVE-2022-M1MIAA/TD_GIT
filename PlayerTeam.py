from Team import Team


class PlayerTeam(Team):


    def __init__(self,members):
        super.__init__(members)
        self.__nb_warriors
        self.__nb_hunters 
        self.__nb_wizards
        self.__damage
        self.__loot
        self.__flee

    def getNbWarriors(self):
        return self.__nb_warriors

    def getNbHunters(self):
        return self.__nb_hunters

    def getNbWizards(self):
        return self.__nb_wizards

    def getDamage(self):
        return self.__damage

    def getLoot(self):
        return self.__loot

    def getFlee(self):
        return self.__flee

    







La classe EnemyTeam hérite de la classe Team et a les attributs privés suivants :

__nb_warriors : int
__nb_hunters : int
__nb_wizatds : int
__damage : int
__loot : int
__flee : int

Elle implémente aussi des méthodes permettant d'accéder aux :

les dégats de l'équipe
la valeur de chance de l'équipe
la valeur de fuite de l'équipe
le nombre de warriors
le nombre de chasseurs
le nombre de magiciens
et la méthode __repr__ si nécessaire