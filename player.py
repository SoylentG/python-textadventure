from colorama import init, Fore, Back, Style
from settings import Settings
from weapon import Weapon
from potion import Potion
import time,sys
from random import uniform

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
        self.triedWalk = False
        self.alive = True
        self.settings = Settings()

    def is_alive(self):
        return self.hp > 0

    def is_in_room(self):
        return self.is_in_room

    def takeDamage(self, damage, monster):
        self.hp -= damage
        if self.hp >=0:
            return "You take"+Fore.RED +" "+ str(damage) +" "+ Style.RESET_ALL +"damage.\n"+\
            Fore.CYAN +self.name+ Style.RESET_ALL + " your HP is now at "+ Fore.CYAN + str(self.getHP()) + Style.RESET_ALL +"\n"
        else:
            return self.die(monster)

    def lvlUp(self):
        print "goal: "+ self.settings.getGoal()
        self.level +=1
        print "lvl: "+ str(self.level)
        if self.level >= self.settings.getGoal():
            print "won"
            self.victory = True
        else:
            print "\nCongratulations "+Fore.CYAN+self.name+Style.RESET_ALL+", you leveled up!\n"

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
        if isinstance(item,Weapon):
            return self.equipItem(len(self.inventory)-1,item)

    def equipItem(self,pos,item):
        slot = pos
        self.equipped = self.inventory[slot]
        string = "You now have "+Fore.YELLOW+self.inventory[slot].name+Style.RESET_ALL+" in your hand."
        if isinstance(item,Weapon):
            self.strength = 1
            self.strength += self.equipped.damage
        else:
            string += "\nDo you want to"+Fore.CYAN+" drink "+Style.RESET_ALL+"it?"
        return string

    def heal(self):
        if isinstance(self.equipped,Potion):
            if not self.equipped.isEmpty:
                self.equipped.drink()
                heal = int(self.hp*self.equipped.strength)
                if self.hp + heal <= 100:
                    self.hp += heal
                    return "You healed "+str(heal)
                else:
                    self.hp = 100
                    return "You are now at full health"
            else:
                return "It's empty."

        elif isinstance(self.equipped,list):
            return "You can't drink air..."
        else:
            return "You can't drink "+self.equipped.name

    def die(self, monster):
        if monster is not None:
            string = "%s takes one last swing at you... The air escapes your lungs and a metallic taste fills your mouth\n \
            One last thought rushes into your mind, screaming and trying to escape your mouth \n"%(monster.getShortName())
        else:
            string = "This was too much...  The air escapes your lungs and a metallic taste fills your mouth\n \
            One last thought rushes into your mind, screaming and trying to escape your mouth \n"
        for char in string:
            time.sleep(uniform(0.05, 0.1))
            sys.stdout.write('\033[35m'+char)
            sys.stdout.flush()
        stringtwo = "Do not forget me..."
        for char in stringtwo:
            time.sleep(uniform(0.6, 1))
            sys.stdout.write('\033[33m'+char)
            sys.stdout.flush()
        self.alive = False
        return Style.RESET_ALL+"\nYou are dead.\n\n"+Fore.CYAN+"restart "+Style.RESET_ALL+"or"+Fore.CYAN+"exit?"

    def getStrength(self):
        return self.strength


    def printInventory(self):
        string = "You own: "
        for index,item in enumerate(self.inventory, start=1):
             string = string+Fore.YELLOW+item.name+Style.RESET_ALL+"[" + str(index) +"], "
        string = string + "\nType"+Fore.CYAN +" equip 1 "+Style.RESET_ALL+"to equip the first item form the list."
        return string

    #    return self.inventory[0].name + self.inventory[1].name
