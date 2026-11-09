import unittest

# from . import Calculator
from . import Calculator

# Assuming the Calculator class and helper functions are defined above 
# or imported from your module (e.g., `from calculator import Calculator, as_num, factorize`)

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Since Calculator is a singleton, this always returns the same instance
        self.calc = Calculator()

    def test_singleton_pattern(self):
        """Verify that Calculator implements the Singleton pattern correctly."""
        calc1 = Calculator()
        calc2 = Calculator()
        self.assertIs(calc1, calc2, "Calculator instances must be identical (Singleton)")

    def test_add(self):
        """Test addition with integers, floats, and numeric strings."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)
        self.assertEqual(self.calc.add("two", "three"), 5)
        self.assertEqual(self.calc.add(None, 5), 5)

    def test_sub(self):
        """Test subtraction with various argument types."""
        self.assertEqual(self.calc.sub(10, 4), 6)
        self.assertEqual(self.calc.sub("ten", "four"), 6)
        self.assertEqual(self.calc.sub(5.5, 2.0), 3.5)

    def test_mul(self):
        """Test multiplication with various argument types."""
        self.assertEqual(self.calc.mul(3, 4), 12)
        self.assertEqual(self.calc.mul("three", "four"), 12)
        self.assertEqual(self.calc.mul(None, 5), 0)

    def test_div(self):
        """Test division and zero-division error handling."""
        self.assertEqual(self.calc.div(10, 2), 5.0)
        # Test division by zero returning infinity as per implementation
        self.assertEqual(self.calc.div(5, 0), float('inf'))
        self.assertEqual(self.calc.div("ten", "two"), 5.0)

    def test_multilingual_string_conversion(self):
        """Test number word conversion across different languages and formats."""
        # English
        self.assertEqual(self.calc.add("five", "five"), 10)
        # German
        self.assertEqual(self.calc.add("fünf", "fünf"), 10)
        self.assertEqual(self.calc.add("fuenf", "eins"), 6)
        # Spanish
        self.assertEqual(self.calc.add("cinco", "dos"), 7)
        # Russian
        self.assertEqual(self.calc.add("пять", "два"), 7)
        # Chinese
        self.assertEqual(self.calc.add("五", "二"), 7)
        # Roman Numerals
        self.assertEqual(self.calc.add("v", "ii"), 7)
        self.assertEqual(self.calc.add("X", "i"), 11)

    def test_invalid_string_conversion(self):
        """Test that invalid strings default to 0."""
        self.assertEqual(self.calc.add("not_a_number", 5), 5)

    def test_factorize(self):
        """Test the prime factorization logic."""
        self.assertEqual(self.calc.factorize(12), [2, 2, 3])
        self.assertEqual(self.calc.factorize(13), [13]) # Prime number
        self.assertEqual(self.calc.factorize(1), [])   # Edge case for 1


if __name__ == '__main__':
    unittest.main()
