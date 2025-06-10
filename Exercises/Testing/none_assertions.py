import unittest

class NoneTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(None, None)

if __name__ == '__main__':
    unittest.main()