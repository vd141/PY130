import unittest

class NoExperienceError(Exception):
    pass

class Employee():
    def __init__(self):
        self.no_experience = True

    @property
    def hire(self):
        if self.no_experience:
            raise NoExperienceError

class TestException(unittest.TestCase):
    def test_exception(self):
        emp = Employee()
        with self.assertRaises(NoExperienceError):
            emp.hire

if __name__ == "__main__":
    unittest.main()