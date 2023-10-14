import sys

[print(path) for path in sys.path]
print()
# $ poetry run python run.py
# /Users/tosh2230/project/pycon-apac-2023
# /opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
# /opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11
# /opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload
# /Users/tosh2230/Library/Caches/pypoetry/virtualenvs/unpacking-module-not-found-error-tiYZ59tI-py3.11/lib/python3.11/site-packages


# Import greetings from src
import src.greetings as greetings  # noqa: E402

greetings.greet_all()
