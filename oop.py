class Monster:

    color = "black"

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.is_innocent = False

    def steal(self, warrior):
        warrior.lose_stick()
