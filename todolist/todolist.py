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

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    return todo_list

# Code omitted

def step_1():
    print('--------------------------------- Step 1')
    todo_list = setup()

    # setup() uses `todo_list.add` to add 3 todos

    try:
        todo_list.add(1)
    except TypeError:
        print('TypeError detected')    # TypeError detected

    for todo in todo_list._todos:
        print(todo)

# step_1()

def step_2():
    print('--------------------------------- Step 2')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

# step_2()

def step_3():
    print('--------------------------------- Step 3')
    todo_list = setup()

    print(len(todo_list))              # 3
    print(len(empty_todo_list))        # 0

# step_3()

def step_4():
    print('--------------------------------- Step 4')
    todo_list = setup()

    print(todo_list.first())           # [ ] Buy milk
    print(todo_list.last())            # [ ] Go to gym

    try:
        empty_todo_list.first()
    except IndexError:
        print('Expected IndexError: Got it!')

    try:
        empty_todo_list.last()
    except IndexError:
        print('Expected IndexError: Got it!')

# step_4()

def step_5():
    print('--------------------------------- Step 5')
    todo_list = setup()

    print(empty_todo_list.to_list())    # []

    todos = todo_list.to_list()
    print(type(todos).__name__)         # list

    for todo in todos:
        print(todo)                     # [ ] Buy milk
                                        # [X] Clean room
                                        # [ ] Go to gym

# step_5()

def step_6():
    print('--------------------------------- Step 6')
    todo_list = setup()

    print(todo_list.todo_at(0))        # [ ] Buy milk
    print(todo_list.todo_at(1))        # [X] Clean room
    print(todo_list.todo_at(2))        # [ ] Go to gym

    try:
        todo_list.todo_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    # Ensure we have a reference
    print(todo_list.todo_at(1) is todo_list.todo_at(1))  # True

# step_6()

def step_7():
    print('--------------------------------- Step 7')
    todo_list = setup()

    todo_list.mark_done_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_done_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_done_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    try:
        todo_list.mark_done_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.mark_undone_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_undone_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [X] Go to gym

    todo_list.mark_undone_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    try:
        todo_list.mark_undone_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

# step_7()

def step_8():
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

step_8()

def step_9():
    print('--------------------------------- Step 9')
    todo_list = setup()

    print(todo_list.all_done())         # False

    todo_list.mark_all_done()
    print(todo_list.all_done())         # True

    todo_list.mark_undone_at(1)
    print(todo_list.all_done())         # False

    print(empty_todo_list.all_done())   # True

# step_9()

def step_10():
    print('--------------------------------- Step 10')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.remove_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    todo_list.remove_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk

    try:
        todo_list.remove_at(1)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.remove_at(0)
    print(todo_list)
    # ---- Today's Todos -----

# step_10()

def step_11():
    print('--------------------------------- Step 11')
    todo_list = setup()

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    def done_if_y_in_title(todo):
        if 'y' in todo.title:
            todo.done = True

    todo_list.each(done_if_y_in_title)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [ ] Clean room
    # [X] Go to gym

    todo_list.each(lambda todo: print('>>>', todo))
    # >>> [X] Buy milk
    # >>> [ ] Clean room
    # >>> [X] Go to gym

# step_11()

def step_12():
    print('--------------------------------- Step 12')
    todo_list = setup()

    def y_in_title(todo):
        return 'y' in todo.title

    print(todo_list.select(y_in_title))
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    print(todo_list.select(lambda todo: todo.done))
    # ---- Today's Todos -----
    # [X] Clean room

# step_12()

def step_13():
    print('--------------------------------- Step 13')
    todo_list = setup()

    todo_list.add(Todo('Clean room'))
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym
    # [ ] Clean room

    found = todo_list.find_by_title('Go to gym')
    print(found)
    # [ ] Go to gym

    found = todo_list.find_by_title('Clean room')
    print(found)
    # [X] Clean room

    try:
        todo_list.find_by_title('Feed cat')
    except IndexError:
        print('Expected IndexError: Got it!')

# step_13()

def step_14():
    print('--------------------------------- Step 14')
    todo_list = setup()

    done = todo_list.done_todos()
    print(done)
    # ----- Today's Todos -----
    # [X] Clean room

    undone = todo_list.undone_todos()
    print(undone)
    # ----- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    done = empty_todo_list.done_todos()
    print(done)
    # ----- Nothing Doing -----

    undone = empty_todo_list.undone_todos()
    print(undone)
    # ----- Nothing Doing -----

# step_14()

def step_15():
    print('--------------------------------- Step 15')
    todo_list = setup()

    todo_list.mark_done('Go to gym')
    print(todo_list)
    # ----- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [X] Go to gym

    try:
        todo_list.mark_done('Feed cat')
    except IndexError:
        print('Expected IndexError: Got it!')

# step_15()

# def test_todo():
#     todo1 = Todo('Buy milk')
#     todo2 = Todo('Clean room')
#     todo3 = Todo('Go to gym')
#     todo4 = Todo('Clean room')

#     print(todo1)                  # [ ] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [ ] Clean room

#     print(todo2 == todo4)         # True
#     print(todo1 == todo2)         # False
#     print(todo4.done)             # False

#     todo1.done = True
#     todo4.done = True
#     print(todo4.done)             # True

#     print(todo1)                  # [X] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [X] Clean room

#     print(todo2 == todo4)         # False

#     todo4.done = False
#     print(todo4.done)             # False
#     print(todo4)                  # [ ] Clean room

# test_todo()