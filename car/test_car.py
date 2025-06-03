import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_wheels(self):
        car = Car()
        self.assertEqual(4, car.wheels)
    
    @unittest.skip('Skipping the color test.')
    def test_color(self):
        car = Car()
        self.assertEqual('blue', car.color)

    def test_bad_wheels(self):
        car = Car()
        self.assertEqual(3, car.wheels)

if __name__ == '__main__':
    unittest.main()

