import sys

print()
[print(path) for path in sys.path]
# /Users/tosh2230/project/pycon-apac-2023/tests/greetings_error
# /Users/tosh2230/Library/Caches/pypoetry/virtualenvs/unpacking-module-not-found-error-tiYZ59tI-py3.11/bin
# /opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
# /opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11
# /opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload
# /Users/tosh2230/Library/Caches/pypoetry/virtualenvs/unpacking-module-not-found-error-tiYZ59tI-py3.11/lib/python3.11/site-packages

from src.greetings_error.friends.cat import Cat  # noqa: E402


def test_greet():
    cat = Cat()
    assert cat.greet() == "Meow"
