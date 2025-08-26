class SimpleLinkedList:
    pass

class Element:
    # initializes with a datum
    # stores the datum in a property called datum
    # has a method is_tail() which returns True by default
    # has a next property which is None by default
    # has an optional second argument that points to the next object in the list
    def __init__(self, datum, next_element=None):
        self._datum = datum
        self._next_element = next_element
        self._is_tail = False if next_element else True

    @property
    def datum(self):
        return self._datum
    
    @property
    def next(self):
        return self._next_element
    
    def is_tail(self):
        return self._is_tail
    
class SimpleLinkedList:
    def __init__(self):
        self._size = 0
        self._is_empty = True
        self._list = []
        self._head = None

    @property
    def size(self):
        return len(self._list)
    
    def is_empty(self):
        return len(self._list) == 0
    
    def push(self, datum):
        if self.is_empty():
            self._head = Element(datum)
            self._list.append(datum)
        else:
            self._head = Element(datum, self._head)
            self._list.insert(0, datum)
    
    def peek(self):
        return self.head.datum if not self.is_empty() else None
    
    def pop(self):
        self._head = self.head.next
        return self._list.pop(0)
    
    @property
    def head(self):
        return self._head
    
    @classmethod
    def from_list(cls, new_list):
        new_sll = cls()
        if new_list:
            for datum in new_list[::-1]:
                new_sll.push(datum)
        return new_sll
    
    def to_list(self):
        return self._list
    
    def reverse(self):
        return SimpleLinkedList.from_list(self._list[::-1])