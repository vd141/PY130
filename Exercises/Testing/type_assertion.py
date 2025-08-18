class NumericSuperClass:
    pass

class Numeric(NumericSuperClass):
    pass

import unittest

class NumericTest(unittest.TestCase):
    def test_numeric(self):
        value = Numeric()
        self.assertIsInstance(value, Numeric)
        self.assertNotIsInstance(value, NumericSuperClass)

if __name__ == "__main__":
    unittest.main()