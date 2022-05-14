class Monster:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def steal(self, warrior):
        warrior.lose_stick()
        