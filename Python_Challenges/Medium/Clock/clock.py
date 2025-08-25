'''
Create a clock that is independent of date.

You should be able to add minutes to and subtract minutes from the time 
represented by a given Clock object. Note that you should not mutate Clock 
objects when adding and subtracting minutes -- create a new Clock object.

Two clock objects that represent the same time should be equal to each other.

You may not use any built-in date or time functionality; just use arithmetic operations.
'''

'''
clock has one class method: at
    takes one or two arguments: hour and minute value
has a __Str__ method that prints 24hour time
has an __add__ method that adds minutes to the current clock time (input is int)
    and returns a new clock instance of that time (does not mutate original time)
    any value at or over 60 is automatically calculated into the hours
    automatically calculates into the next day's time if input time goes over
has a __sub__ method that subtracts minute sto current clock time (input is int)
    and returns a new clock instance of time (does not miutate original time)
    any value at or under 60 is automatically calculated into the hours
    automatically calculates into the next day's time if input time goes under
'''

class Clock:
    def __init__(self):
        self._hours = None
        self._minutes = None
    
    @classmethod
    def at(cls, *time):
        return_me = cls()
        if len(time) == 2:
            return_me._hours, return_me._minutes = time
        if len(time) == 1:
            return_me._hours, return_me._minutes = time, 0
        return return_me

    def __str__(self):
        return f'{self._hours:02.0f}:{self._minutes:02.0f}'

    def __eq__(self, other):
        return (self._hours == other._hours and self._minutes == other._minutes)
    
