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
