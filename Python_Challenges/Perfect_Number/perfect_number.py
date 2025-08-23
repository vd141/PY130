# write a program that can tell whether a number is perfect, abundant, or deficient
# according to its aliquot sum

# perfect number: a number that is equal to the sum of its proper divisors
# abundant number: a number that is less than the sum of its proper divisors
# deficient number: a number that is greater than the sum of its proper divisors

class PerfectNumber():
    @classmethod
    def classify(cls, target):
        if target > 0:
            factors = [potential_factor for potential_factor in range(1, target)
                       if target % potential_factor == 0]
            sum_factors = sum(factors)
            match sum_factors:
                case _ if sum_factors < target:
                    return 'deficient'
                case _ if sum_factors == target:
                    return 'perfect'
                case _ if sum_factors > target:
                    return 'abundant'
        else:
            raise ValueError('Input must be a positive integer')

