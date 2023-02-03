from random import randint
class Die():

    def __init__(self):
        self.sides = 10

    def roll_die(self):
        randon = randint(1, self.sides)
        print(f"numero randomico: {randon}")


dado = Die()
i = 0
while i < 10:
    dado.roll_die()
    i +=1
