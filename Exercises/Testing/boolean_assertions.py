import unittest

class ValueTest(unittest.TestCase):
    def test_value(self):
        value = 4
        self.assertTrue(value % 2 != 0)

if __name__ == '__main__':
    unittest.main()