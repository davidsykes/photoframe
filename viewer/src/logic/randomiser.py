import random

class Randomiser:
    def choices(self, choices, weights):
        return random.choices(
            choices,
            weights=weights,
            k=1)[0]

    def random(self, range):
        return random.randrange(0, range)