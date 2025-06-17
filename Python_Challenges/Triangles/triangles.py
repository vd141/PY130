'''
write a program to determine whether a triangle is equilateral,
isoceles, or scalene

for any shape to be a triangle, all sides must be of length > 0,
and the sum of the lengths of any two sides must be greater than
the length of the third side

PEDAC - problem, examples, data structures, algorithm, code

inputs: lengths of 3 sides as 3 separate arguments in the Triangle constructor
outputs: error if triangle is invalid, triangle type in the .kind attribute
    if the triangle sides are valid

create a method to check validity of inputs

if inputs are valid, determine what type of triangle it is

'''

class Triangle:
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._sides = {side1, side2, side3}
        if not self._is_valid():
            raise ValueError
        self._determine_kind()

    def _is_valid(self):
        if any(side <= 0 for side in self._sides):
            return False
        sides_list = [self._side1, self._side2, self._side3]
        for side in sides_list:
            if side >= sum(sides_list) - side:
                return False
        return True
    
    def _determine_kind(self):
        if len(self._sides) == 1:
            self._kind = 'equilateral'
        if len(self._sides) == 2:
            self._kind = 'isosceles'
        if len(self._sides) == 3:
            self._kind = 'scalene'

    @property
    def kind(self):
        return self._kind