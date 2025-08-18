import unittest

class BooleanTest(unittest.TestCase):
    def test_boolean(self):
        value = 2
        self.assertTrue(value % 2 != 0)

if __name__ == "__main__":
    unittest.main()