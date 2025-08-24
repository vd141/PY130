# a Triangle instance will alwayas be initialized with 3 sides, which can be floats
# Triangle has one public method, kind() which returns a lowercase string of the 
# triangle type
#
# tirnagle instance will throw a valueError when initialized if the input sides 
# are invalid
# ValueError if:
#   any side is less than or equal to zero
#   sum of any two sides is less than or equal to the third side
#
# public method kind() uses the length of a set to determine the triangle type

class Triangle:
    def __init__(self, *sides):
            if self._is_valid(sides):
                  self._side_set = set(sides)
            else:
                  raise ValueError("Invalid triangle side(s)! Ensure all triangle" \
                  "sides are valid.")
            
    @property
    def kind(self):
          unique_sides = len(self._side_set)
          match unique_sides:
                case 1:
                      return 'equilateral'
                case 2:
                      return 'isosceles'
                case 3:
                      return 'scalene'
                
    def _is_valid(self, sides):
        # check side values
        # sides is a tuple, so convert to a list
        sides = list(sides)
        if any(side <= 0 for side in sides):
            return False
        # check side sums
        for side in sides:
            remaining = sides.copy()
            remaining.remove(side)
            sum_remaining = sum(remaining)
            if side >= sum_remaining:
                    return False
        return True
    
# think through problem before coding with a predetermined data struct
# list remove() method returns None
# there are two sub problems in these challenges: 1: the algorithm and 2: the 
#   implementation to pass the test (know how to define classes)
# 1. analyze test cases (does object need to be initialized to use method or is
#    it simply a class method, how many inputs, what inputs are allowed, how
#    are public methods called, what are their return values)
# 2. write scaffold for class (but don't implement yet!)
# 3. then go into algorithm implementation (and fit into scaffold from last step)
# 4. scaffold may need some refinement as you progress