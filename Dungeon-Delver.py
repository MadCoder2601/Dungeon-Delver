import random

from time import sleep

import sys

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Declare all your classes first

class Player1:

  def __init__(self, playerclass):

    self.classname = playerclass[0]

    self.health = playerclass[1]

    self.attack = playerclass[2]

    self.defense = playerclass[3]

 

 

class Monster:

  def __init__(self, stats):

    self.name = stats[0]

    self.health = stats[1]

    self.attack = stats[2]

    self.defense = stats[3]

    self.desc = stats[4]

 

# Next define all your functions

def monsterSetup():

  monster_list = ["goblin", "troll", "orc"]

  monster_choice = monster_list[random.randint(0,2)]

 

  # [0] = Monster Name, [1] = Monster Health, [2] = Monster Attack, [3] Monster Defense, [4] = Monster Description

 

  if monster_choice == "goblin":

    monster = ["goblin", 25, 10, 5, "Goblin"]

  elif monster_choice == "troll":

    monster = ["Troll", 50, 13, 7, "Troll"]

  elif monster_choice == "orc":

    monster = ["Orc", 75, 15, 10, "Orc"]

  else:

    monster = ["Glitch", 100, 100, 100, "Glitch"]

 

  return Monster(monster)

 

def fightSequence(player, monster):
  
    encounter = 1

    turn = 'player'

    print("A Wild " + monster.desc + " Appeared!")

    sleep(2)

    while encounter == 1:

        if turn == 'player':

            clear()
          
            print("Player Health: " + str(player.health))

            print("Monster Health: " + str(monster.health))

            action = input("What would you like to do (Attack)? ")

            action = action.lower()

            if action == 'attack':
              roll = random.randint(1,20)
              if roll >= monster.defense:
                print("You Hit!")
                sleep(0.3)
                monster.health = monster.health - player.attack

                print("You Dealt " + str(player.attack) + " Damage!")
                if monster.health <= 0:

                  sleep(0.3)
                  print("You Killed The " + monster.desc + "!")
                  fightSequence(player, monsterSetup())

                  return True

                turn = 'monster'
              else:
                print("You Missed!")
                if monster.health <= 0:

                  print("You Killed The " + monster.desc + "!")
                  clear()
                  
                  fightSequence(player, monsterSetup())

                  return True

                turn = 'monster'

        elif turn == 'monster':
          clear()
          roll = random.randint(1,20)
          if roll >= player.defense:
            print("The " + monster.desc + " hit you!")
            sleep(0.3)
            player.health = player.health - monster.attack
            print("The " + monster.desc + " Did " + str(monster.attack) + " Damage!")
            if (player.health == 0) or (player.health < 0):

              clear()
              
              print("You Died!")

              quit(1)

            turn = 'player'
            
          else:
            print("The " + monster.desc + " Missed!")
            if (player.health == 0) or (player.health < 0):

              print("You Died!")

              quit(1)

            turn = 'player'

 

global player_health

 

monster = []

 

monster_list = ["Goblin", "Troll", "Orc"]

 

description = "Blank"

 

monsterChoice = monster_list[random.randint(0,2)]

 

 
name = input("Enter your name: ") 

playerChoice = input("What class do you want to be? (Warrior, Archer, Mage)? ")

 

playerChoice = playerChoice.lower()

 

warrior = ["Warrior", 100, 10, 10]

archer = ["Archer", 75, 15, 7]

mage = ["Mage", 50, 20, 5]

villager = ["Villager", 1, 1, 1]

 

 

if playerChoice == "warrior":

  player_class = warrior

elif playerChoice == "archer":

  player_class = archer

elif playerChoice == "mage":

  player_class = mage

else:

  player_class = villager

 

player = Player1(player_class)

 

fightSequence(player, monsterSetup())
