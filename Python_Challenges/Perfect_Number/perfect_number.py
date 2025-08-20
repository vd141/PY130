# write a program that can tell whether a number is perfect, abundant, or deficient
# according to its aliquot sum

# perfect number: a number that is equal to the sum of its proper divisors
# abundant number: a number that is less than the sum of its proper divisors
# deficient number: a number that is greater than the sum of its proper divisors

class PerfectNumber():
    def __init__(self):
        pass

    # classify is a public method that does not take negative numbers
    # if a negative number is passed, it raises a ValueError message
    # that says: "Input must be a positive integer"

    @classmethod
    def classify(number):
        if number <= 0:
            raise ValueError('Input must be a positive integer')
        aliquot_sum = sum(PerfectNumber._get_factors(number))

        match aliquot_sum:
            case _ if aliquot_sum < number:
                return 'deficient'
            case _ if aliquot_sum > number:
                return 'abundant'
            case _ if aliquot_sum == number:
                return 'perfect'

    def _get_factors(number):
        # loop through all numbers from 1 to number and add number to factors list
        # if the number is divisible by the factor

        return [factor for factor in range(1, number) if number % factor == 0]