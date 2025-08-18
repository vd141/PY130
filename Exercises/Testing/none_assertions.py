import unittest

class NoneTest(unittest.TestCase):
    def test_none(self):
        value = None
        self.assertIsNone(value)

if __name__ == "__main__":
    unittest.main()