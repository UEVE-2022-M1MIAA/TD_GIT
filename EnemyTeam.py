from Team import Team

class EnemyTeam(Team):
  def __init__(self, unit, members):
    super().__init__(members)
    
    self.__unit = unit
    self.__damage = 0
    self.__loot = 0
  
  def get_unit(self):
    return self.__unit
  
  def get_damage(self):
    return self.__damage
  
  def get_loot(self):
    return self.__loot