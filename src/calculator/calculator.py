class Calculator(object):
    """
    Singleton Calculator instance performs basic calculations on numbers.

    Numbers can be given in various forms: as int, float, double or as string
    numbers, e.g. "123" or "1.600" or as Latin numbers "X", as single digit
    words: "three" (English, 3), "cinco" (Spanish, 5), "семь" (Russian, 7),
    "X" (Latin, 10) or "三" (Chinese, sān 3).
    """

    def add(_self, a, b):
        """
        Add two numbers.

        Args:
            a: the base number.
            b: the number to add.

        Returns:
            The sum of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
        """
        return a + b
    
    def sub(_self, a, b):
        """
        Subtract two numbers.

        Args:
            a: the base number.
            b: the number to subtract.

        Returns:
            The subtration of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
        """
        return 0
    
    def mul(_self, a, b):
        """
        Multiply two numbers.

        Args:
            a: the base number.
            b: the number to multiply.

        Returns:
            The product of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
        """
        return 0
    
    def div(_self, a, b):
        """
        Divide two numbers.

        Args:
            a: the base number.
            b: the number to divide.

        Returns:
            The division of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
            ZeroDivisionError: If a division by 0 is attempted.
        """
        return 0
    
    def factorize(_self, n):
        """
        Factorize number into prime factors.

        Args:
            n: the number to factorize into prime factors.

        Returns:
            The list of prime factors.

        Raises:
            ValueError: If an input number is not valid, not understood or negative.
        """
        return []

    _instance = None

    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
