import unittest

class ObjectAssertionTest(unittest.TestCase):
    def setUp(self):
        self.list_of_strings = ['asdf',
                           'jthgfbcv',
                           'bart',
                           'xyz']
    def test_in(self):
        self.assertIn('xyz', self.list_of_strings)

    def test_not_in(self):
        self.assertNotIn('xyz', self.list_of_strings)

if __name__ == "__main__":
    unittest.main()