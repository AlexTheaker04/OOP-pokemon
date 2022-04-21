import random
class Monster:
    def __init__(self, name, type, health, damage, defence, ):
        self.name = name
        self.type = type
        self.health = health
        self.damage = damage
        self.defence = defence

    def attack(self, target):
        print("attack")
        target.attacked(self.damage)

    def s_attack(self, target):
        print("special attack")

    def heal(self):
        print("heal")

    def retreat(self):
        print()

    def print_stats(self):
        print(self.name, self.type, self.health, self.damage, self.defence)

    def view_stats(self):
        Monster1.print_stats()
        Monster2.print_stats()

    def attacked(self, damage):
        print("ouch")
        self.health = self.health - damage


print("Welcome to the battle!")
print("*****************************")
print("""
In this game, you have to fight against either the computer or another player. You take turns attacking or healing your
Monster. You can enter either "attack", "heal" or "retreat"
""")
computer = 0
monster_classes = ["fire", "water", "earth"]
choice = input("do you want to play against the computer (Y) or another player (N) ? : ")
choice = choice.upper()

name1 = input("Player 1, what name do you want for your monster? ")
type1 = input("Player, what type (fire, earth, water:? ")
health1 = int(input("Player what health:? "))
damage1 = int(input("how much damage:? "))
defence1 = int(input("How much defence:? "))
Monster1 = Monster(name1, type1, health1, damage1, defence1)

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
    health2 = random.randint(30, 50)
    damage2 = random.randint(30, 50)
    defence2 = random.randint(30, 50)
    Monster2 = Monster(name2, type2, health2, damage2, defence2)

if computer == 1:
    while True:
        # user portion doing things
        Monster1.view_stats()
        p_input = input("player what do you want to do? (attack, heal, retreat) ? ")
        if p_input == "1":
            Monster1.attack(Monster2)
        elif p_input == "2":
            Monster1.view_stats()


        # computer taking actions
        Monster2.attack(Monster1)


        if Monster1.health <= 0:
            print("Computer wins ")
            break
        elif Monster2.health <= 0:
            print("Player wins ")
            break
