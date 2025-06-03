import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # your tests go here
    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        # todos.to_list returns a shallow copy of its list

        # check that to_list() returns a list
        self.assertEqual(type(self.todos.to_list()), list)

        # check that to_list() returnvalue is equal to todos' private list
        self.assertEqual(self.todos.to_list(), self.todos._todos)

    def test_first(self):
        # check if the first value of the todo list is equal and the same
        # object as the first todo object
        self.assertEqual(self.todos.first(), self.todo1)
        self.assertIs(self.todos.first(), self.todo1)

    def test_last(self):
        pass

if __name__ == "__main__":
    unittest.main()