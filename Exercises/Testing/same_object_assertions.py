import unittest

class LstClass():
    @property
    def process(self):
        return tuple()

class SameObjectTest(unittest.TestCase):
    def test_same_object(self):
        lst = LstClass()
        self.assertIs(lst, lst.process)

if __name__ == "__main__":
    unittest.main()