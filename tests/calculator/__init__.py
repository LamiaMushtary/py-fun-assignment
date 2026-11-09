# Gemini: What is the purpose of an empty __init__.py ?
# 
# 1. Enabling Package Imports (Python < 3.3)
# Historically, Python required an __init__.py file in every directory of
# a hierarchical package structure. Without it, Python would treat the folder
# as a regular directory and refuse to let you import modules from it using
# dot notation.
# 
# 2. Supporting Implicit Namespace Packages (Python 3.3+)
# Since Python 3.3, implicit namespace packages were introduced via PEP 420.
# This means Python can now recognize a directory as a package even if it
# does not contain an __init__.py file.

from context import Calculator
