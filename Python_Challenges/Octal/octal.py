# implement octal to decimal conversion
# input: octal string
# output: decimal string
# invalid inputs are octal 0
# octal numbers are made up of digits 0-7

class Octal():
    # an instance of octal is initialized with a decimal string
    # when the public method to_decimal() is called, the octal number is
    # returned, as an int
    def __init__(self, octal):
        self._octal = octal

    def to_decimal(self):
        # octal number is a string
        # loop through the string from right to left, convert each char
        # to an int, and multiply it by the appropriate power of 8
        # at the end of each loop, add the value to an accumulator (to be returned)
        # 
        # validity check: check if the input string is octal
        # all digits of input string must be 0-7
        if self._valid():
            accumulator = 0
            power = 0
            for digit in self._octal[::-1]:
                accumulator += int(digit) * (8 ** power)
                power += 1
            return accumulator
        return 0

    def _valid(self):
        for digit in self._octal:
            try: 
                if int(digit) not in range(8):
                    return False
            except ValueError:
                return False
        return True
    
print(Octal('2047').to_decimal())