from ..util.message import format


class Cat:
    def __init__(self):
        self.phrase = "meow"

    def greet(self):
        return format(self.phrase)
