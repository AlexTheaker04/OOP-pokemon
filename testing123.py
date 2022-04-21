import random


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

    def attack(self, target):
        # print("attack")
        target.attacked(self.damage)

    def s_attack(self, target):
        print("special attack")
        target.attacked(self.damage + 5)

    def heal(self):
        temp = self.health
        self.health += temp * .2

    def retreat(self):
        print()

    def print_stats(self):
        print(self.name, self.type, self.health, self.damage, self.defence)

    def view_stats(self):
        Monster1.print_stats()
        Monster2.print_stats()

    def attacked(self, damage):
        # print("ouch")
        self.health = self.health - damage


class earth(Monster):
    def s_attack(self, target):
        print("special attack")
        target.attacked(self.damage + 10)


class water(Monster):
    print("Water")

    def heal(self):
        temp = self.health
        self.health += (temp * .2) + 10


class fire(Monster):

    def __init__(self, name, type, health, damage, defence):
        super().__init__(name, type, health, damage, defence + 5)


print("Welcome to the battle!")
print("*****************************")
print("""
In this game, you have to fight against either the computer or another player.
You take turns attacking or healing your Monster. You can enter either "attack",
 "heal" or "retreat"
""")
computer = 0
monster_classes = ["fire", "water", "earth"]
choice = input("do you want to play against the computer (Y) or another player (N) ? : ")
choice = choice.upper()
health1 = 0
damage1 = 0
defence1 = 0

while True:  # validation
    print("Remember, points cannot be more then 50!")
    name1 = input("Player 1, what name do you want for your monster? ")
    type1 = input("Player, what type (fire, earth, water:? ")
    health1 = int(input("Player what health:? "))
    damage1 = int(input("how much damage:? "))
    defence1 = int(input("How much defence:? "))

    if health1 + damage1 + defence1 < 51:
        Monster1 = fire(name1, type1, health1, damage1, defence1)
        break


if choice == "N":
    name2 = input("Player 2, what name do you want for your monster?")
    type2 = input("Player, what type (fire, earth, water):? ")
    health2 = int(input("Player what health:? "))
    damage2 = int(input("how much damage:? "))
    defence2 = int(input("How much defence:? "))
    Monster2 = Monster(name2, type2, health2, damage2, defence2)
else:
    computer = 1
    name2 = "El Computer"
    type2 = random.choice(monster_classes)
    health2 = random.randint(1, 30)
    damage2 = random.randint(5, 10)
    defence2 = random.randint(3, 10)
    if type2 == "fire":
        Monster2 = fire(name2, type2, health2, damage2, defence2)
    elif type2 == "water":
        Monster2 = water(name2, type2, health2, damage2, defence2)
    else:
        Monster2 = earth(name2, type2, health2, damage2, defence2)
heal = 1
if computer == 1:
    while True:
        # user portion doing things
        Monster1.view_stats()
        p_input = int(input(
            "player what do you want to do? (attack (1), heal (3), retreat or view stats (2) , special attack (4) ? "))
        if p_input == 1:
            Monster1.attack(Monster2)
        elif p_input == 4:
            Monster1.s_attack(Monster2)
        elif p_input == 2:
            Monster1.view_stats()
        if p_input == 3 and heal == 1:
            print("healing HP")
            Monster1.heal()
            heal = 0
        elif p_input == 3 and heal == 0:
            print("you cant heal :(")
            break

        # computer taking actions
        # Monster2.attack(Monster1)

        if Monster1.health <= 0:
            print("Computer wins ")
            break
        elif Monster2.health <= 0:
            print("Player wins ")
            break
        # AI retreat
        if Monster2.health <=5 and random.randint(1,10) == 5:
            Monster2.retreat()
            print(" Monster 2 has retreated, you win!")

