class WalkingStick:
    pass

from abc import ABC, abstractmethod

class Warrior(ABC):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.is_mobile = True
        self.stick = WalkingStick()

    @abstractmethod
    def walk(self):
        pass

class NormalWarrior(Warrior):
    def walk(self):
        print("Walking")

class SuperWarrior(Warrior):
    def fight(self):
        print("Fighting")
        return 225

    def walk(self):
        while self.is_mobile:
            print("Walk without REST")

n_warrior = NormalWarrior(15, 'WoR')
print(n_warrior.name)

s_warrior = SuperWarrior(22, 'SoR')
print(s_warrior.fight())