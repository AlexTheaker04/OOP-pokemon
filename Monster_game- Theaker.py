import random
import time


# Program Header
# Program Name: Assignment - monster game
# Programmer: Alex Theaker
# Date: april 29, 2022,
# Input: user will input names and stats of monsters, and what they want their monsters to do.
# Output: 4 encrypted messages output to the console, each on a separate line, and saved to a file

class Monster:
    def __init__(self, name, type, health, damage, defence, ):  # set variables
        self.name = name
        self.type = type
        self.health = health
        self.damage = round((.4 * damage), 2)
        self.defence = defence

    def attack(self, target, target2):
        # print("attack")
        target.attacked(self.damage, target2)

    def s_attack(self, target, target2):
        target.attacked(self.damage + 2, target2)

    def heal(self):
        self.health += 5

    def retreat(self, name):
        print(name, "has retreated, you win!")
        quit()

    def print_stats(self):
        print(self.name, ": ", "Type: ", self.type, ", health: ", round(self.health, 2), ", Attack: ",
              round(self.damage, 2), ", Defence: ", round(self.defence, 2))
        print("*------*")

    def view_stats(self):
        print("*----stats----*")
        Monster1.print_stats()
        Monster2.print_stats()

    def attacked(self, damage, target2):
        print(self.health, "before health")
        self.health = self.health - damage
        print(self.health, "after health")
        print(str(target2), "was hit for ", damage)


class earth(Monster):
    def s_attack(self, target, target2):
        target.attacked(self.damage + 5, target2)
    # self.damage + 5


class water(Monster):
    # better healing
    def heal(self):
        self.health += 10


class fire(Monster):
    # increase defence by 3
    def __init__(self, name, type, health, damage, defence):
        super().__init__(name, type, health, damage, defence + 3)


def end_game(name):
    print(name, " won! thanks for playing!")
    quit()


print("Welcome to the battle!")
print("*****************************")
print("""
In this game, you have to fight against either the computer or another player.
You take turns attacking or healing your Monster. You can enter either "attack",
 "heal", special attack  or "retreat"
 - As a earth type, you get 5 more damage to its special attack
 - As a fire type you get 3 more defence 
 - As a water you get 5 more HP when healing.
""")
computer = 0
monster_classes = ["fire", "water", "earth"]

# if user wants to play against computer or other player
choice = input("Do you want to play against the computer (Y) or another player (N) ? : ")
choice = choice.upper()

while choice != "Y" and choice != "N":
    print("try again!")
    choice = input("Do you want to play against the computer (Y) or another player (N) ? : ")
    choice = choice.upper()

health1 = damage1 = 0
# damage1 = 0
defence1 = 0
health2 = 0
damage2 = 0
defence2 = 0
heal = 1
heal2 = 1
special_count = 1
special_count2 = 1

while True:  # setting player values and monster type, incl validation.
    print("Set your monsters abilities. Remember, total points cannot be more then 50!")
    name1 = input("Player 1, what name do you want for your monster? ")
    type1 = input("Player, what type (fire, earth, water):? ")
    while type1 not in ["fire", "earth", "water"]:
        print("error, must be either fire, earth or water")
        type1 = input("Player, what type (fire, earth, water):? ")
    health1 = int(input("What health:? "))
    damage1 = int(input("how much damage:? "))
    defence1 = int(input("How much defence:? "))

    if health1 + damage1 + defence1 < 51 and name1 != "":
        if type1 == "fire":
            Monster1 = fire(name1, type1, health1, damage1, defence1)
        elif type1 == "water":
            Monster1 = water(name1, type1, health1, damage1, defence1)
        else:
            Monster1 = earth(name1, type1, health1, damage1, defence1)
        break
    print("error, try again!")
if choice == "N":
    while True:  # setting player values and monster type, incl validation.
        print("Set your monsters abilities. Remember, total points cannot be more then 50!")
        name2 = input("Player 2, what name do you want for your monster? ")
        type2 = input("Player 2, what type (fire, earth, water):? ")
        while type2 not in ["fire", "earth", "water"]:
            print("error, must be either fire, earth or water")
            type2 = input("Player 2, what type (fire, earth, water):? ")
        health2 = int(input("What health:? "))
        damage2 = int(input("how much damage:? "))
        defence2 = int(input("How much defence:? "))

        if health2 + damage2 + defence2 < 51 and name2 != "":
            if type2 == "fire":
                Monster2 = fire(name2, type2, health2, damage2, defence2)
            elif type2 == "water":
                Monster2 = water(name2, type2, health2, damage2, defence2)
            else:
                Monster2 = earth(name2, type2, health2, damage2, defence2)
            break
else:
    while True:
        # set random  computer monster stats for computer
        computer = 1
        name2 = "El Computer"
        type2 = random.choice(monster_classes)
        health2 = random.randint(15, 30)
        damage2 = random.randint(9, 20)
        defence2 = random.randint(10, 15)

        if health2 + damage2 + defence2 < 51:
            if type2 == "fire":
                Monster2 = fire(name2, type2, health2, damage2, defence2)
            elif type2 == "water":
                Monster2 = water(name2, type2, health2, damage2, defence2)
            else:
                Monster2 = earth(name2, type2, health2, damage2, defence2)
            break
if computer == 1:  # if playing against computer
    while True:
        print("")
        print("")
        print("")
        # health check for both monsters
        if Monster1.health <= 0:
            end_game("Computer")
        elif Monster2.health <= 0:
            end_game("Player 1")
        Monster1.view_stats()
        while True:  # user portion doing things

            p_input = input("player 1, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                            "special attack (4)? ")
            while not p_input.isdigit():
                print("not a number, try again!")
                p_input = input(
                    "player 1, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                    "special attack (4)? ")

            p_input = int(p_input)

            if p_input == 1:
                Monster1.attack(Monster2, name2)
                break
            if p_input == 4 and special_count != 0:
                Monster1.s_attack(Monster2, name2)
                special_count -= 1
                break
            if p_input == 4:
                print("you can only special attack once!")
            if p_input == 2:
                Monster1.view_stats()
            if p_input == 3 and heal == 1:
                print("healing 5 HP")
                Monster1.heal()
                heal = 0
                break
            if p_input == 5:
                Monster1.retreat(name1)
            elif p_input == 3 and heal == 0:
                print("you cant heal :(")

            print("error, try again")

        # computer taking actions
        time.sleep(0)
        # health check for both monsters
        if Monster1.health <= 0:
            end_game("Computer")
        elif Monster2.health <= 0:
            end_game("Player")
        if random.randint(1, 4) == 1:
            Monster2.s_attack(Monster1, name1)
        else:
            Monster2.attack(Monster1, name1)
        # AI retreat
        if Monster2.health <= 5 and random.randint(1, 10) == 5:
            Monster2.retreat(name2)
        elif Monster2.health <= 5:
            Monster2.heal()

if computer == 0:  # if playing against other players.
    while True:
        print("")
        print("")
        print("")
        Monster1.view_stats()
        # health check for both monsters
        if Monster1.health <= 0:
            end_game("Player 2")
        elif Monster2.health <= 0:
            end_game("Player 1")
        while True:  # user p 1moves

            p_input = input("player 1, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                            "special attack (4)? ")
            while not p_input.isdigit():
                print("not a number, try again!")
                p_input = input(
                    "player 1, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                    "special attack (4)? ")
            p_input = int(p_input)
            if p_input == 1:
                Monster1.attack(Monster2, name2)
                break
            if p_input == 4 and special_count != 0:
                Monster1.s_attack(Monster2, name2)
                special_count -= 1
                break
            if p_input == 2:
                Monster1.view_stats()
            if p_input == 3 and heal == 1:
                print("healing HP")
                Monster1.heal()
                heal = 0
                break
            if p_input == 5:
                Monster1.retreat(name1)
            elif p_input == 3 and heal == 0:
                print("you cant heal :(")

        # user 2 moves
        print("")
        print("")
        print("")
        Monster2.view_stats()

        if Monster1.health <= 0:
            end_game("Player 2")
        elif Monster2.health <= 0:
            end_game("Player 1")
        while True:  # user 2 moves
            p_input = input("player 2, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                            "special attack (4)? ")
            while not p_input.isdigit():
                print("not a number, try again!")
                p_input = input(
                    "player 1, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                    "special attack (4)? ")
            p_input = int(p_input)
            if p_input == 1:
                Monster2.attack(Monster1, name1)
                break
            if p_input == 4 and special_count != 0:
                Monster2.s_attack(Monster1, name1)
                special_count2 -= 1
                break
            if p_input == 2:
                Monster2.view_stats()
            if p_input == 3 and heal == 1:
                print("healing HP")
                Monster2.heal()
                heal = 0
                break
            if p_input == 5:
                Monster2.retreat(name2)
            elif p_input == 3 and heal == 0:
                print("you cant heal :(")
