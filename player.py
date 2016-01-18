from colorama import init, Fore, Back, Style
class Player(object):

    def __init__(self):
    	self.name = "a"
        self.hp = 100
        self.facesMonster = False
        self.victory = False
        self.condition = "normal"
        self.strength = 1
        self.armor = 1
        self.level = 1
        self.inventory =[]
        self.hasItems=False
        self.is_in_room = False
        self.equipped = []


    def is_alive(self):
        return self.hp > 0

    def is_in_room(self):
        return self.is_in_room

    def takeDamage(self, damage):
        self.hp -= damage
        return "You take"+Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage."

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.condition = condition

    def is_facing_Monster(self):
        return self.facesMonster

    def facing_Monster(self, status):
        self.facesMonster = status

    def addItem(self, item):
        self.inventory.append(item)
        self.hasItems = True
        return self.equipItem(len(self.inventory)-1)

    def equipItem(self,item):
        slot = item

        self.equipped = self.inventory[slot]
        self.strength = 1
        self.strength += self.equipped.damage
        return "You now use "+Fore.YELLOW+self.inventory[slot].name+Style.RESET_ALL

    def getStrength(self):
        return self.strength


    def printInventory(self):
        string = "You own: "
        for index,item in enumerate(self.inventory, start=1):
             string = string+item.name+"[" + str(index) +"], "
        string = string + "\nType"+Fore.CYAN +" equip 1 "+Style.RESET_ALL+"to equip the first item form the list."
        return string

    #    return self.inventory[0].name + self.inventory[1].name
