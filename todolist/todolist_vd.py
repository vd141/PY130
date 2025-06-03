'''
todo list
'''

class Todo:
    COMPLETE = 'X'
    INCOMPLETE = ' '
    def __init__(self, task_name):
        self._done = False
        self._task_name = task_name.capitalize()

    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, complete_status):
        if not isinstance(complete_status, bool):
            return NotImplemented
        self._done = complete_status
    
    @property
    def title(self):
        return self._task_name
    
    def __str__(self):
        indicator = Todo.COMPLETE if self.done else Todo.INCOMPLETE
        return f'[{indicator}] {self.title}'
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return ((self.title == other.title) and 
        (self.done == other.done))
    
class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    def __str__(self):
        return_str = f'---- {self.title} ----\n'
        for todo in self._todos:
            return_str += str(todo) + '\n'
        return return_str
    
    def __len__(self):
        return len(self._todos)

    @property
    def title(self):
        return self._title
    
    def add(self, todoitem):
        if not isinstance(todoitem, Todo):
            raise TypeError('Argument must be a Todo object.')
        self._todos.append(todoitem)

    def first(self):
        '''
        returns first item in todo list
        '''
        if not self._todos:
            raise IndexError('List is empty. First item unretrievable.')
        return self._todos[0]
    
    def last(self):
        '''
        returns last item in todo list
        '''
        if not self._todos:
            raise IndexError('List is empty. Last item unretrievable.')
        return self._todos[-1]
    
    def to_list(self):
        '''
        returns copy of todo list
        '''
        return self._todos.copy()
    
    def todo_at(self, index):
        '''
        returns todo item at index
        '''
        try:
            return self._todos[index]
        except IndexError as e:
            raise IndexError(f'{e}: Index must be in bounds.')
        
    def mark_done_at(self, index):
        try:
            self._todos[index].done = True
        except IndexError as e:
            raise IndexError(f'{e}: Index must be in bounds.')

    def mark_undone_at(self, index):
        try:
            self._todos[index].done = False
        except IndexError as e:
            raise IndexError(f'{e}: Index must be in bounds.')
        
    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True
        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False
        self.each(mark_undone)

    def all_done(self):
        return all([task.done for task in self._todos])
    
    def remove_at(self, position):
        try:
            self._todos.pop(position)
        except IndexError as e:
            raise IndexError(f'Index must be in bounds.')
        
    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        selected = TodoList(self.title)
        def choose(todo):
            if callback(todo):
                selected.add(todo)
        self.each(choose)
        return selected
    
    def find_by_title(self, search_term):
        # takes a string as an argument and returns the first Todo object whose 
        # title equals the argument. raise an indexerror if no matching Todos
        # are found. if multiple matching todos are found, return just the first
        # for item in self._todos:
        #     if item.title == search_term:
        #         return item
        try:
            found = self.select(lambda todo: todo.title == search_term)
            return found.todo_at(0)
        except IndexError as e:
            raise IndexError(f'{e}: Search term not found!')
        
    def done_todos(self):
        '''
        returns selected todolist of completed todos. if there are no completed
        todos, returns empty todolist
        '''
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        '''
        returns selected todolist of incomplete todos. if there are no incomplete
        todos, returns empty todolist
        '''
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        '''
        takes a string as argument and marks the first item that matches the
        string as done. raise an indexerror if no matching todo is found
        '''
        self.find_by_title(title).done = True
