from randommonstername import RandomMonsterName
from player import Player
from actions import Actions as actions
from settings import Settings
from monster import Monster
from room import Room
from colorama import init, Fore, Back, Style
import random
import re
import sys

init()

def play():
    settings = Settings()
    difficulty = settings.difficulty
    player = Player()

    print ("What is your name?\n")
    name_input = raw_input ('>: ')
    player.name = name_input
#
# Asks for the player Name
#
    print Style.RESET_ALL
    print '{:^90}'.format("Hello"+Fore.CYAN + " %s"%(player.name) + Style.RESET_ALL +"!")
    print '{:^80}'.format("Welcome to our world of pain and suffering!")


#
# Game Loop start
#
    while player.is_alive() and not player.victory:


        if not player.is_in_room:
            room = Room(difficulty,player)
            player.is_in_room = True

        print ("\nWhat do you want to do?\n")

    #
    # Asks the player for some Input commands
    #
        action_input = raw_input(Fore.CYAN + player.name+ '>: ')

        if room.is_done() and action_input.lower() == "continue":
            response = actions(action_input,player,room)
            print response
            room = room.getRoom(difficulty,player)
        elif action_input.lower() == "restart":
            print Back.WHITE+"                  "+Fore.BLACK+"Game restarted"+ Back.WHITE +Fore.RED+"                  \n"+Style.RESET_ALL
            play()
        elif action_input.lower() == "exit":
            print Back.RED+"                  "+Fore.WHITE+"Game exited"+ Back.RED +"                  \n"+Style.RESET_ALL
            break;
        else:
            # The magic happens here:
            response = actions(action_input,player,room)
            if player.condition is "normal":
                string = str(response)
            #    print Back.WHITE+Fore.WHITE+Style.BRIGHT+string
                print response
            elif player.condition is "poisoned":
                #Do stuff with "response"
                string = re.sub(r"(.\d*.[\[].)","",str(response)[::-1])

                print string

if __name__ == "__main__":
    play()
