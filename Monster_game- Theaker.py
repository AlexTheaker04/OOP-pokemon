import random


# Program Header
# Program Name: Assignment - monster game
# Programmer: Alex Theaker
# Date: april 29, 2022,
# Input: user will input names and stats of monsters, and what they want their monsters to do.
# Output: 4 encrypted messages output to the console, each on a separate line, and saved to a file

# earth gets 5 bonus to special attack
# fire gets 5 more to defence
# water get 5 more to heal

class Monster:
    def __init__(self, name, type, health, damage, defence, ):
        self.name = name
        self.type = type
        self.health = health
        self.damage = damage
        self.defence = defence

    def attack(self, target, target2):
        # print("attack")
        target.attacked(self.damage, target2, )

    def s_attack(self, target, target2):
        target.attacked(self.damage, target2)

    def heal(self):
        temp = self.health
        self.health += temp * .2

    def retreat(self, name):
        print(name, "has retreated, you win!")
        quit()

    def print_stats(self):
        print(self.name, ": ", "Type: ", self.type, ", health: ", self.health, ", Attack: ",
              self.damage, ", Defence: ", self.defence)
        print("*------*")

    def view_stats(self):
        print("*----stats----*")
        Monster1.print_stats()
        Monster2.print_stats()

    def attacked(self, damage, target2):
        self.health = self.health - damage
        print(str(target2), "was hit for ", damage)


class earth(Monster):
    def s_attack(self, target, target2):
        target.attacked(self.damage + 10, target2)
    # self.damage + 10


class water(Monster):
    # better healing
    def heal(self):
        temp = self.health
        self.health += (temp * .2) + 10


class fire(Monster):
    # increase defence by 5
    def __init__(self, name, type, health, damage, defence):
        super().__init__(name, type, health, damage, defence + 5)


def end_game(name):
    print(name, " won! thanks for playing!")
    quit()


print("Welcome to the battle!")
print("*****************************")
print("""
In this game, you have to fight against either the computer or another player.
You take turns attacking or healing your Monster. You can enter either "attack",
 "heal", special attack  or "retreat"
""")
computer = 0
monster_classes = ["fire", "water", "earth"]
choice = input("Do you want to play against the computer (Y) or another player (N) ? : ")
choice = choice.upper()
health1 = 0
damage1 = 0
defence1 = 0
health2 = 0
damage2 = 0
defence2 = 0
heal = 1
heal2 = 1
special_count = 1
special_count2 = 1

while True:  # validation
    print("Set your monsters abilities. Remember, total points cannot be more then 50!")
    name1 = input("Player 1, what name do you want for your monster? ")
    type1 = input("Player, what type (fire, earth, water):? ")
    health1 = int(input("What health:? "))
    damage1 = int(input("how much damage:? "))
    defence1 = int(input("How much defence:? "))

    if health1 + damage1 + defence1 < 51:
        if type1 == "fire":
            Monster1 = fire(name1, type1, health1, damage1, defence1)
        elif type1 == "water":
            Monster1 = water(name1, type1, health1, damage1, defence1)
        else:
            Monster1 = earth(name1, type1, health1, damage1, defence1)
        break
    print("error, try again!")
if choice == "N":
    name2 = input("Player 2, what name do you want for your monster?")
    type2 = input("Player, what type (fire, earth, water):? ")
    health2 = int(input("Player what health:? "))
    damage2 = int(input("how much damage:? "))
    defence2 = int(input("How much defence:? "))
    Monster2 = Monster(name2, type2, health2, damage2, defence2)
else:
    while True:
        # set computer monster stats for computer
        computer = 1
        name2 = "El Computer"
        type2 = random.choice(monster_classes)
        health2 = random.randint(20, 30)
        damage2 = random.randint(9, 20)
        defence2 = random.randint(10, 15)

        if health2 + damage2 + defence2 < 52:
            if type2 == "fire":
                Monster2 = fire(name2, type2, health2, damage2, defence2)
            elif type2 == "water":
                Monster2 = water(name2, type2, health2, damage2, defence2)
            else:
                Monster2 = earth(name2, type2, health2, damage2, defence2)
            break
if computer == 1:
    while True:

        print("")
        print("")
        print("")
        # health check for both monsters
        if Monster1.health <= 0:
            end_game("Player 2")
        elif Monster2.health <= 0:
            end_game("Player 1")
        Monster1.view_stats()
        while True:  # user portion doing things

            p_input = int(input("player what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                                "special attack (4)? "))
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
                break

        # computer taking actions

        # health check for both monsters
        if Monster1.health <= 0:
            end_game("Computer")
        elif Monster2.health <= 0:
            end_game("Player")
        # attacking
        if random.randint(1, 4) == 1:
            Monster2.s_attack(Monster1, name1)
        else:
            Monster2.attack(Monster1, name1)
        # AI retreat
        if Monster2.health <= 5 and random.randint(1, 10) == 5:
            Monster2.retreat(name2)
        else:
            Monster2.heal()

if computer == 0:
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
        while True:  # user portion doing things

            p_input = int(
                input("player 1, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2) , "
                      "special attack (4)? "))
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
                break

        # user 2 moves
        print("")
        print("")
        print("")
        Monster2.view_stats()
        while True:  # user 1 moves

            p_input = int(input("player 2, what do you want to do? (attack (1), heal (3), retreat (5), view stats (2), "
                                "special attack (4)? "))
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
                break
