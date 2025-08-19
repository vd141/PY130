'''
write a program to convert decimal numbers to Roman numerals

assume inputs range from 1-3000 (4 digits max)

convert input to string, then determine roman numerals for reach
digit from left to right

for first digit, check full length of string. if len is 4, use M for the
number of the digit. if 3, use CM for 900 and above and D for 400 and above.
use 
'''

class RomanNumeral:
    def __init__(self, decimal):
        self._decimal = decimal
    
    