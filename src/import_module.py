import os
import importlib
from pathlib import Path
# 
# Programmatic module import (.py file) from alternatives. If present,
# 'preferred_mod' is imported, otherwise 'default_mod'.
# Keyword arguments:
# calling_file -- '__file__' parameter in calling file
# default_mod -- name of default module (.py file) to import
# preferred_mod -- name of preferred module (.py file) to import (default None)
# return -- imported module
def import_module(calling_file:str, default_mod: str, preferred_mod:str=None):
    p, a = Path(calling_file).parent, os.path.abspath(os.curdir)
    mp=str(p.relative_to(a)).replace('\\', '/').replace('/', '.')
    mod=preferred_mod if preferred_mod else default_mod
    if mod:
        try:
            return importlib.import_module(mp + '.' + mod)
        # 
        except ImportError:
            return import_module(calling_file, default_mod, None)
