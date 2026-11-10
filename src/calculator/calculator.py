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
        #return a + b
        return _self._as_number(a) + _self._as_number(b) #converting strings to numbers before adding them
    
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
        #return 0
        return _self._as_number(a) - _self._as_number(b)
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
        #return 0
        return _self._as_number(a) * _self._as_number(b)
    
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
        #return 0
        return _self._as_number(a) / _self._as_number(b)
    
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
        #return []
        
        n = _self._as_number(n)

        if isinstance(n, float) and n.is_integer():
            n = int(n)

        if not isinstance(n, int) or n <= 0:
            raise ValueError("factorize expects a positive integer")

        factors = []
        divisor = 2

        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1

        if n > 1:
            factors.append(n)

        return factors
    
    @staticmethod
    def _as_number(value):
        # Leave numbers such as int and float values unchanged.
        if not isinstance(value, str):
            return value

        # Ignore accidental spaces and make word matching case-insensitive.
        text = value.strip()
        normalized = text.casefold()

        # Try ordinary integer strings first, such as "1".
        try:
            return int(text)
        except ValueError:
            pass

        # Then try decimal strings, such as "1.600".
        try:
            return float(text)
        except ValueError:
            pass

        # These are the single digit names required for this assignment.
        word_to_number = {
            # English
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,

            # German (include both common spellings of "five").
            "null": 0, "eins": 1, "ein": 1, "zwei": 2, "drei": 3,
            "vier": 4, "fünf": 5, "fuenf": 5, "sechs": 6, "sieben": 7,
            "acht": 8, "neun": 9,

            # Spanish
            "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
            "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,

            # Russian
            "ноль": 0, "нуль": 0, "один": 1, "два": 2, "три": 3,
            "четыре": 4, "пять": 5, "шесть": 6, "семь": 7,
            "восемь": 8, "девять": 9,

            # Chinese
            "零": 0, "〇": 0, "一": 1, "二": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
        }

        # Return the mapped value, or explain which input was not recognized.
        if normalized in word_to_number:
            return word_to_number[normalized]
        
        # The assignment examples use Roman numerals from I through X.
        roman_to_number = {
            "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
            "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
        }

        # upper() makes lowercase forms such as "viii" work too.
        if text.upper() in roman_to_number:
            return roman_to_number[text.upper()]

        raise ValueError(f"Not a recognized number: {value!r}")

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
