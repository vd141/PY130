# initializes with a year and month (both as numbers)
# has one public method called day() that takes a case insensitive weekday and
# a case insensitive occurrence of the month

from datetime import date, timedelta

class Meetup:
    WEEKDAY_INDEX = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }

    OCCURRENCE = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3,
        'fifth': 4,
        'last': -1,
        'teenth': {13, 14, 15, 16, 17, 18, 19},
    }

    def __init__(self, year, month):
        self._year = year
        self._month = month

    def day(self, weekday, occurrence):
        # we know the year and the month, use the weekday and occurrence to find
        # the exact day
        # return day as a date object with (year, month, day) as arguments
        # if such a weekday/occurrence does not exist, return None
        # in datetime, weekdays are indexed from 0-6 for Monday-Sunday
        # isoweekday indexes from 1-7 for Monday-Sunday
        # gather all days of the month in which the weekday index matches the weekday
            # loop through all the days of the month. if the weekday value of that day
            # matches the input, add it to a list
            # to find the days of the month, subtract one from the next month
        # then use the occurrence to select the appropriate day from the list
        # if the occurrence is teenth, convert the list into a set and deterimine
        # if there is an intersection of any of the teenth values. 
        # return that intersection if so

        # to get the days in a given month, subtract 1 from the next month.
        # but if the current month is 12, need to subtract 1 from the first month
        # of the following year
        weekday = weekday.casefold()

        next_month = 0 if self._month == 12 else self._month
        next_year = self._year if next_month != 0 else self._year + 1

        days_in_month = (date(next_year, next_month + 1, 1) -
                         timedelta(days=1)).day
        
        day_ranges = range(1, days_in_month + 1)

        valid_days = []

        for day in day_ranges:
            if (date(self._year, self._month, day).weekday() == 
                self.__class__.WEEKDAY_INDEX[weekday]):
                valid_days.append(day)
        
        if occurrence.casefold() != 'teenth':
            occurrence_index = self.__class__.OCCURRENCE[occurrence.casefold()]
            num_valid_days = len(valid_days)
            day_date = (valid_days[occurrence_index] if 
                    ((occurrence_index < num_valid_days) and 
                     (num_valid_days != 0)) else None)
        else:
            intersection = set(valid_days).intersection(self.__class__.OCCURRENCE['teenth'])
            if intersection:
                for day in intersection:
                    day_date = day
                    break
            else:
                day_date = None

        return date(self._year, self._month, day_date) if day_date else None
        


# Meetup(2025, 8).day('wednesday', 'first')