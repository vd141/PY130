# implement octal to decimal conversion
# input: octal string
# output: decimal string
# invalid inputs are octal 0
# octal numbers are made up of digits 0-7

class Octal:
    def __init__(self, input_str):
        self._input_str = input_str
    
    def to_decimal(self):
        if not self._verify(self._input_str):
            return 0
        decimal = 0
        # loop through octal string from right to left (or reversed octal str)
        # enumerate reversed octal string. index is the power of 8
        # add decimal value to decimal accumulator
        for index, octal in enumerate(self._input_str[::-1]):
            decimal += int(octal) * (8 ** index)
        return decimal

    def _verify(self, input_str):
        for char in input_str:
            if char not in '01234567':
                return False
        return True