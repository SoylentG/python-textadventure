from weapon import Weapon
from potion import Potion
from gold import Gold

class Items():

    def __init__(self):
        self.weapon = Weapon()
        self.potion = Potion()
        #self.gold = Gold()

    def randomWeapon(self, value):
        if value < 5:
            self.weapon.name = "a Knife"
            self.weapon.setValue = 1
            self.weapon.damage = 7
            return self.weapon
        if value <7:
            self.weapon.name = "a Shoe"
            self.weapon.setValue = 1
            self.weapon.damage = 2
            return self.weapon
        else:
            self.weapon.name = "a Sword"
            self.weapon.setValue = 5
            self.weapon.damage = 10
            return self.weapon

    def newPotion(self,strength,uses):
        print "potion!"
        self.potion.strength = strength
        self.potion.uses = uses
        return self.potion
