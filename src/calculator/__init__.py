# export class 'Calculator' from local module './calculator.py'
from .calculator import Calculator

# from src.import_module import import_module
# # # export class 'Calculator' from local module './calculator.py'
# # # or, if present, from implementation module './calculator_impl.py'
# mod=import_module(__file__, 'calculator', 'calculator_impl')
# Calculator=mod.Calculator

# export 'main()' from local './main.py'
from .main import main
