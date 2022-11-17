import random


class Hunter:
    def __init__(self):
        self.degat = random.choice([1, 2])
        self.luck = 10
        self.fuite = 20
        self.prix = 25
        self.unite = "hunter"
