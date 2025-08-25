'''
robot must come up with a random name of this format: r'^[A-Z]{2}\d{3}$'

instance property 'name' returns such a name and the same name every time it is
called

different instances of Robot should return different names

robot has a reset() public instance method that gives the robot a new name when called


'''

import random

class Robot:
    names = set()

    def __init__(self):
        self.reset()

    @property
    def name(self):
        return self._name

    def reset(self):
        # characters A-Z take on chr values 65-90
        # digits 0-9 take on chr values 48 to 57
        # loop three times to produce two letters
        # loop twice to produce three digits
        while True:
            name = ''
            for _ in range(2):
                name += chr(random.choice(range(65, 91)))
            for _ in range(3):
                name += chr(random.choice(range(48, 58)))
            if name not in self.__class__.names:
                break
        self._name = name
        self.__class__.names.add(name)