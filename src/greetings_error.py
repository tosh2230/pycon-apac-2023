# "src/greetings_error/__init__.py" does not exist, python can't find greetings_error package.
#
# $ poetry run python src/greetings_error.py
# Traceback (most recent call last):
#   File "/Users/tosh2230/project/pycon-apac-2023/src/greetings_error.py", line 5, in <module>
#     from greetings_error.cat import Cat
#   File "/Users/tosh2230/project/pycon-apac-2023/src/greetings_error.py", line 5, in <module>
#     from greetings_error.cat import Cat
# ModuleNotFoundError: No module named 'greetings_error.cat'; 'greetings_error' is not a package

from src.greetings_error.friends.cat import Cat
from src.greetings_error.friends.dog import Dog
from src.greetings_error.friends.human import Human


def greet_all():
    friends = [
        Cat(),
        Dog(),
        Human(),
    ]
    [print(friend.greet()) for friend in friends]


if __name__ == "__main__":
    greet_all()
