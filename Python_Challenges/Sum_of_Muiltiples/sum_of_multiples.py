'''
Write a program that, given a natural number and a set of one or more other 
numbers, can find the sum of all the multiples of the numbers in the set that 
are less than the first number. If the set of numbers is not given, use a 
default set of 3 and 5.

For instance, if we list all the natural numbers up to, but not including, 20 
that are multiples of either 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18. The
sum of these multiples is 78.

for each number in the set, find all multiples up to the natural number
add them to a set (removes duplicates)

how to find all multiples? starting with the first number, add multiples of that
number until the sum is greater than the natural number
'''

class SumOfMultiples():
    _set_num = [3, 5]

    def __init__(self, *set_num):
        # set_num should take any number of arguments and default to 3,5
        self._set_num = set_num

    @classmethod
    def sum_up_to(cls, target_natural):
        cls._target_natural = target_natural
        all_multiples = set()
        for num in cls._set_num:
            all_multiples.update(cls._all_up_to_target(num))
        return sum(all_multiples)

    def to(self, target_natural):
        self._target_natural = target_natural
        all_multiples = set()
        for num in self._set_num:
            all_multiples.update(self._all_up_to_target_instance(num))
        return sum(all_multiples)
    
    def _all_up_to_target_instance(self, num):
        accumulator = 0
        multiples = []
        while True:
            accumulator += num
            if accumulator < self._target_natural:
                multiples.append(accumulator)
                continue
            break
        return multiples

    @classmethod
    def _all_up_to_target(cls, num):
        accumulator = 0
        multiples = []
        while True:
            accumulator += num
            if accumulator < cls._target_natural:
                multiples.append(accumulator)
                continue
            break
        return multiples
