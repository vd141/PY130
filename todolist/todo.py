'''
requirements:
each todo item has a state consisting of a title and a completed mark
    both state attributes should be defined as properties
    both properties should have a getter
    only the completed mark should have a setter
'''

class Todo:
    DONE = 'X'
    NOT_DONE = ' '
    def __init__(self, title):
        self._title = title
        self._done = False

    def __str__(self):
        marker = Todo.DONE if self.done else Todo.NOT_DONE
        return f'[{marker}] {self.title}'
    
    def __eq__(self, other):
        if not isinstance(other,Todo):
            raise NotImplementedError
        
        return (True if (other.title == self.title and other.done == self.done)
                else False)

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, is_done):
        self._done = is_done