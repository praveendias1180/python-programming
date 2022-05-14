class Monster:

    color = "black"

    def __init__(self, age, name):
        self.age = age
        self.name = name

        # private properties
        self._is_innocent = False

    def steal(self, warrior):
        warrior.lose_stick()

monster_1 = Monster(15, "mOn")
monster_2 = Monster(15, "MoN")

print(monster_1.age)
print(monster_1._is_innocent)
print(type(monster_2))