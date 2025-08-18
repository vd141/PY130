# import unittest
# from car import Car

# class CarTest(unittest.TestCase):
#     @unittest.skip('Skipping this one!')
#     def test_wheels(self):
#         car = Car()
#         self.assertEqual(3, car.wheels)

# if __name__ == "__main__":
#     unittest.main(verbosity=2)

# import class to test
# import unittest
# initialize a test class that inherits from unittest.TestCase
# create an init function
# initialize a car instance
# use test class instance method (self.assertEqual) to test that the car's wheel attribute
# is equal to some number
# create a __name__ == "__main__" block that runs unittest's main() method if
# the test file is run as a script

import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_wheels(self):
        car = Car()
        self.assertEqual(car.wheels, 4)

if __name__ == "__main__":
    unittest.main()