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
    def task_name(self):
        return self._task_name
    
    def __str__(self):
        indicator = Todo.COMPLETE if self.done else Todo.INCOMPLETE
        return f'[{indicator}] {self.task_name}'
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return ((self.task_name == other.task_name) and 
        (self.done == other.done))
    
class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    def __str__(self):
        return_str = '---- Today\'s Todos ----\n'
        for todo in self._todos:
            return_str += str(todo) + '\n'

        return return_str

    @property
    def title(self):
        return self._title
    
    def add(self, todoitem):
        if not isinstance(todoitem, Todo):
            raise TypeError('Argument must be a Todo object.')
        self._todos.append(todoitem)

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

step_2()

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