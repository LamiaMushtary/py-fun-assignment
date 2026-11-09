# __init__.py executes when the package (this folder) is imported for the
# first time from another module. It is good practice to not include logic
# in __init__.py, but what is exported from the package.

from .calculator import main, Calculator
# from .collections import main, Collection
