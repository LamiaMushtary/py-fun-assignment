
class Calculator(object):
    """
    Singleton Calculator instance performs basic calculations on numbers.

    Numbers can be given in various forms: as int, float or strings,
    including number words and Roman numerals.
    """

    def add(_self, a, b):
        """Add two numbers."""
        return _self._as_number(a) + _self._as_number(b)

    def sub(_self, a, b):
        """Subtract two numbers."""
        return _self._as_number(a) - _self._as_number(b)

    def mul(_self, a, b):
        """Multiply two numbers."""
        return _self._as_number(a) * _self._as_number(b)

    def div(_self, a, b):
        """Divide two numbers."""
        a = _self._as_number(a)
        b = _self._as_number(b)

        if b == 0:
            return float("inf")

        return a / b

    def factorize(_self, n):
        """Factorize a positive integer into prime factors."""
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
        # Treat None and unrecognized strings as zero.
        if value is None:
            return 0

        if not isinstance(value, str):
            return value

        text = value.strip()
        normalized = text.casefold()

        if not text:
            return 0

        # Integer and decimal strings.
        try:
            return int(text)
        except ValueError:
            pass

        try:
            return float(text)
        except ValueError:
            pass

        word_to_number = {
            # English
            "zero": 0, "one": 1, "two": 2, "three": 3,
            "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9, "ten": 10,

            # German
            "null": 0, "eins": 1, "ein": 1, "zwei": 2,
            "drei": 3, "vier": 4, "fünf": 5, "fuenf": 5,
            "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
            "zehn": 10,

            # Spanish
            "cero": 0, "uno": 1, "dos": 2, "tres": 3,
            "cuatro": 4, "cinco": 5, "seis": 6,
            "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,

            # Russian
            "ноль": 0, "нуль": 0, "один": 1, "два": 2,
            "три": 3, "четыре": 4, "пять": 5, "шесть": 6,
            "семь": 7, "восемь": 8, "девять": 9, "десять": 10,

            # Chinese
            "零": 0, "〇": 0, "一": 1, "二": 2, "三": 3,
            "四": 4, "五": 5, "六": 6, "七": 7,
            "八": 8, "九": 9, "十": 10,
        }

        if normalized in word_to_number:
            return word_to_number[normalized]

        roman_to_number = {
            "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
            "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
        }

        if text.upper() in roman_to_number:
            return roman_to_number[text.upper()]

        # Treat unrecognized strings as zero.
        return 0

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass
