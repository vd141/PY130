
class Series():
    # series is a class that takes a string of a number as an input when initialized
    # add each slice to a parent list and return that parent list
    # has one public instance method caled slices
    def __init__(self, slice_me):
        self._slice_me = slice_me

    def slices(self, slice_length):
        if slice_length > len(self._slice_me):
            raise ValueError('Slice exceeds length of input.')
        parent = []
        # there can be len(input)-slice_len + 1 slices
        for starting_index in range(len(self._slice_me) - slice_length + 1):
            listed = list(self._slice_me[starting_index: 
                                          starting_index + slice_length])
            parent.append([int(elem) for elem in listed])
        return parent