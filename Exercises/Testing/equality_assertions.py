import unittest

class EqualityTest(unittest.TestCase):
    def test_equality(self):
        value = 'XyZ'
        self.assertEqual('xyz', value.lower())

if __name__ == "__main__":
    unittest.main()