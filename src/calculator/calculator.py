
class Calculator(object):
    _instance = None

    def add(_self, a, b):
        return a + b
    
    def sub(_self, a, b):
        return 0
    
    def mul(_self, a, b):
        return 0
    
    def div(_self, a, b):
        return 0
    
    def factorize(_self, n):
        return []

    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
