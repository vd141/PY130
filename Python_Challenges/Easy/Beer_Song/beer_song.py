'''
Write a program that can generate the lyrics of the 99 Bottles of Beer song
'''

class BeerSong():
    @classmethod
    def verse(cls, line):
        return BeerSong._build_first_line(line) + BeerSong._build_second_line(line)
        
    @classmethod
    def _build_first_line(cls, num):
        # returns the correct string given the number of bottles on the wall
        # different lines for cases 2-99, 1, and 0
        if num in range(2, 100):
            return f'{num} bottles of beer on the wall, {num} bottles of beer.\n'
        if num == 1:
            return '1 bottle of beer on the wall, 1 bottle of beer.\n'
        if num == 0:
            return 'No more bottles of beer on the wall, no more bottles of beer.\n'
        
    @classmethod
    def _build_second_line(cls, num):
        # returns the correct string given the number of bottles on the wall
        if num in range(3, 100):
            return f'Take one down and pass it around, {num - 1} bottles of beer on the wall.\n'
        if num == 2:
            return f'Take one down and pass it around, 1 bottle of beer on the wall.\n'
        if num == 1:
            return 'Take it down and pass it around, no more bottles of beer on the wall.\n'
        if num == 0:
            return 'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
        
    @classmethod
    def verses(cls, first_line, second_line):
        verses = []
        for line in range(first_line, second_line - 1, -1):
            verses.append(cls.verse(line))
        return '\n'.join(verses)
    
    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)
        
# class method verse() that returns the verse of the input line (int)
# edge cases for 1 bottle and 0 bottles of beer on the wall

# class method verses() takes two arguments: starting line and ending line and
# prints out all the verses inclusive

# class method lyrics() prints out the lyrics for the whole song