class Character:
    enemyHealth = 20
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.health = 100
        self.attack_power = 10

    def attack(self, enemyName):
        enemyBar = Character.enemyHealth
        if self.attack_power <= enemyBar:
            print(f"{enemyName} has been attacked by {self.name}")
            Character.enemyHealth -= self.attack_power
            print( f"Enemy health remaining is {Character.enemyHealth}" )

    def level_up(self):
        self.level += 10


    def status(self):
        print(f"Name:{self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")



c1 = Character("justine")
c1.attack("goblin")
c1.level_up()
c1.status()