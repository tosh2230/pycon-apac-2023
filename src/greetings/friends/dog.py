from ..util.message import format


class Dog:
    def __init__(self):
        self.phrase = "woof woof"

    def greet(self):
        return format(f"{self.phrase}!")
