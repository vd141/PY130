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

# loop throough all numbers between 1 and target and check to see if they are
# divisible by any numbers in the list. if they are, add them to a new_list to
# be summed and returned

# class state is preserved between test cases because there is no setUp method

class SumOfMultiples:
    def __init__(self, *factors):
        self._factors = factors if factors else (3, 5)

    @classmethod
    def sum_up_to(cls, target):
        return cls().to(target)

    def to(self, target):
        cum_sum = 0
        for i in range(1, target):
            if self._is_a_multiple(i):
                cum_sum += i
        return cum_sum


    def _is_a_multiple(self, num):
        return any(num % factor == 0 for factor in self._factors)