import unittest

class ValueTest(unittest.TestCase):
    def test_boolean(self):
        value = 2
        self.assertTrue(value % 2 != 0, 'Failure message: value is not odd.')

if __name__ == "__main__":
    unittest.main()