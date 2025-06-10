import unittest

class XyzTest(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('word'.lower(), 'xyz')

if __name__ == '__main__':
    unittest.main()