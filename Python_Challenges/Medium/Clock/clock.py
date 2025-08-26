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
            return_me._hours, return_me._minutes = *time, 0
        return return_me

    def __str__(self):
        return f'{self._hours:02.0f}:{self._minutes:02.0f}'

    def __eq__(self, other):
        return (self._hours == other._hours and self._minutes == other._minutes)
    
    def __add__(self, minutes):
        # self. has hours and minutes
        # given minutes to add, add to current minutes value
        # if sum of minutes is greater than 60, divmod sum by 60.
        # get floor value
        #   if floor value + sum is greater than 24, get the result of sum % 24
        #   and make that the sum
        # add the remainder (result of modulo - 2nd output) to the minutes
        sum_minutes = self._minutes + minutes
        sum_hours = self._hours
        if sum_minutes > 60:
            hours, sum_minutes = divmod(sum_minutes, 60)
            sum_hours = hours + self._hours
            if sum_hours >= 24 and sum_minutes >= 0:
                sum_hours = sum_hours % 24
        return self.__class__.at(sum_hours, sum_minutes)

    def __sub__(self, minutes):
        # given minutes, subtract from instance's minutes
        # if the result is negative, divmod the result by 60 to get the new hour
        # and new minutes
        # add the new hour to the current hour
        # if the result is negative, mod the result by 24 to get the true hour
        minute_result = self._minutes - minutes
        new_hour = self._hours
        if minute_result < 0:
            new_hour, new_minutes = divmod(minute_result, 60)
            new_hour = new_hour + self._hours
            if new_hour < 0:
                new_hour = new_hour % 24
            minute_result = new_minutes
        return self.__class__.at(new_hour, minute_result)