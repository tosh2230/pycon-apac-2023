```python
$ poetry run python
Python 3.11.5 (main, Aug 24 2023, 16:05:45) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

# sys.path(First item '' means current directory)
>>> import sys
>>> sys.path
['', '/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip', '/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11', '/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload', '/Users/tosh2230/Library/Caches/pypoetry/virtualenvs/unpacking-module-not-found-error-tiYZ59tI-py3.11/lib/python3.11/site-packages']

# Get module specs
>>> from _frozen_importlib_external import PathFinder
>>> src_spec = PathFinder.find_spec("src")
>>> src_spec
ModuleSpec(name='src', loader=<_frozen_importlib_external.SourceFileLoader object at 0x10249b110>, origin='/Users/tosh2230/project/pycon-apac-2023/src/__init__.py', submodule_search_locations=['/Users/tosh2230/project/pycon-apac-2023/src'])
>>> greetings_spec = PathFinder.find_spec("src.greetings", src_spec.submodule_search_locations, None)
>>> greetings_spec
ModuleSpec(name='src.greetings', loader=<_frozen_importlib_external.SourceFileLoader object at 0x10249ab50>, origin='/Users/tosh2230/project/pycon-apac-2023/src/greetings/__init__.py', submodule_search_locations=['/Users/tosh2230/project/pycon-apac-2023/src/greetings'])

# Create a module object
>>> from importlib.util import module_from_spec
>>> greetings = module_from_spec(greetings_spec)
>>> greetings
<module 'src.greetings' from '/Users/tosh2230/project/pycon-apac-2023/src/greetings/__init__.py'>

# Modules not yet loaded can't be execute
>>> greetings.greet_all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'src.greetings' has no attribute 'greet_all'

# The module object "greetings" does not exists in sys.modules
>>> any([key for key in sys.modules.keys() if key == "src.greetings"])
False

# Load the module object
>>> greetings_loader = greetings_spec.loader
>>> greetings_loader
<_frozen_importlib_external.SourceFileLoader object at 0x1006f7f50>
>>> greetings_loader.exec_module(greetings)

# Execute successfully
>>> greetings.greet_all()
Meow
Woof woof!
Hello. The current time is 2023-10-08 16:09:38.

# src.greetings cached in sys.modules
>>> any([key for key in sys.modules.keys() if key == "src.greetings"])
True
>>>
```
