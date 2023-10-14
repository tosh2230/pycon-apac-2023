from .friends.cat import Cat
from .friends.dog import Dog
from .friends.human import Human


def greet_all():
    friends = (
        Cat(),
        Dog(),
        Human(),
    )
    [print(friend.greet()) for friend in friends]
