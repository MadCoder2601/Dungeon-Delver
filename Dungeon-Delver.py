import random
from time import sleep
import sys

global player_health

monster = []

monster_list = ["Goblin", "Troll", "Orc"]

description = "Blank"

monsterChoice = monster_list[random.randint(0,2)]

class Player():

  def __init__(self, player_health, player_attack, player_defense):
    self.player_health = player_health
    self.player_attack = player_attack
    self.player_defense = player_defense
  
    class Warrior:
        player_health = 100
        player_attack = 10
        player_defense = 10

    class Archer:
        player_health = 75
        player_attack = 15
        player_defense = 7

    class Mage:
        player_health = 50
        player_attack = 20
        player_defense = 5

warrior = ["Warrior", 100, 10, 10]
archer = ["Archer", 75, 15, 7]
mage = ["Mage", 50, 20, 5]

playerChoice = input("What class do you want to be? (Warrior, Archer, Mage)? ")

playerChoice = playerChoice.lower()

if playerChoice == "warrior":
        player_class = warrior
elif playerChoice == "archer":
        player_class = archer
elif playerChoice == "mage":
        player_class = mage

class_name = player_class[0]
player_health = player_class[1]
player_attack = player_class[2]
player_defense = player_class[3]

class Monster:
  def __init__(self, name, health, attack, defense, desc):
    self.name = name
    self.health = health
    self.attack = attack
    self.defense = defense
    self.desc = desc

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
  
  monster_name = monster[0]
  monster_health = monster[1]
  monster_attack = monster[2]
  monster_defense = monster[3]
  monster_description = monster[4]

def fightSequence():
    monster_name = monster[0]
    monster_health = monster[1]
    monster_attack = monster[2]
    monster_defense = monster[3]
    monster_description = monster[4] 
    monsterSetup()
    encounter = 1
    turn = 'player'
    print("A Wild " + monster_description + " Appeared!")
    sleep(2)
    while encounter == 1:
        if turn == 'player':
            print("Player Health: " + str(player_health))
            print("Monster Health: " + str(monster_health))
            action = input("What would you like to do (Attack)? ")
            action = action.lower()
            if action == 'attack':
                monster_health = monster_health - player_attack
                print("You Dealt " + str(player_attack) + " Damage!")
                if monster_health <= 0:
                  print("You Killed The " + str(monster[0]) + "!")
                  fightSequence()
                turn = 'monster'
        elif turn == 'monster':
            player_health = player_health - monster[2]
            print("The " + str(monster[0]) + " Did " + str(monster[2]) + " Damage!")
            if (player_health == 0) or (player_health < 0):
              print("You Died!")
              quit(1)
            turn = 'player'

fightSequence()
